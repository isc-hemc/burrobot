"""burrobot resource module."""

import os
from operator import itemgetter

import requests as http_request
from flask import Response, request
from flask_restful import Resource
from transformers import pipeline
from utils import CustomResponse


class BurrobotResource(Resource):
    """BurrobotResource.

    Resource that expose the QA endpoints. This resource when it's deployed
    trains a model using BERT and the squad2 spanish dataset.

    Attributes
    ----------
    qa : Pipeline
        Suitable pre-trained pipeline for questions and answers tasks.

    Methods
    -------
    get()
        Retrieve the API status.

    """

    qa = pipeline(
        "question-answering",
        model=os.environ.get("BERT_SQUAD_MODEL"),
        tokenizer=os.environ.get("BERT_SQUAD_TOKENIZER"),
    )

    def get(self):
        """GET Request."""
        verify_token = request.args.get("hub.verify_token")
        if verify_token == os.environ.get("WEBHOOK_TOKEN"):
            return int(request.args.get("hub.challenge"))

        return "Unable to authorise."

    def post(self) -> Response:
        """POST Request.

        Makes a HTTP request to retrieve a context and perform an evaluation
        using the `question-answer` pipeline.

        Raises
        ------
        KeyError
            When the payload doesn't has the required keys.

        Returns
        -------
        Response

        """
        payload = request.get_json()

        message = payload["entry"][0]["messaging"][0]["message"]
        sender_id = payload["entry"][0]["messaging"][0]["sender"]["id"]

        cms_api = os.environ.get("CMS_API_HOST")

        context_id = 3

        try:
            res = http_request.get(f"{cms_api}/context/{context_id}").json()
        except Exception:
            return CustomResponse(
                message="Unable to reach the CMS API."
            ).error(404)

        context = res["data"]["description"]

        if message["text"]:
            answer = self.qa(context=context, question=message["text"])

            response_body = {
                "messaging_type": "RESPONSE",
                "recipient": {"id": sender_id},
                "message": {"text": answer["answer"]},
            }

            fb_access_token = os.environ.get("FACEBOOK_PAGE_TOKEN")
            fb_host = (
                "https://graph.facebook.com/v9.0/me/messages?access_token="
            )
            response = http_request.post(
                f"{fb_host}{fb_access_token}", json=response_body
            )

            return response.json()

        return CustomResponse(
            message="Empty Payload: JSON content expected."
        ).error()

        # if not payload:
        #     return CustomResponse(
        #         message="Empty Payload: JSON content expected."
        #     ).error()

        # try:
        #     context_id, question = itemgetter("context_id", "question")(
        #         payload
        #     )
        # except KeyError:
        #     return CustomResponse(
        #         message="context_id or question keys required."
        #     ).error()

        # cms_api = os.environ.get("CMS_API_HOST")

        # try:
        #     res = http_request.get(f"{cms_api}/context/{context_id}").json()
        # except Exception:
        #     return CustomResponse(
        #         message="Unable to reach the CMS API."
        #     ).error(404)

        # context = res["data"]["description"]

        # answer = self.qa(context=context, question=question)

        # return CustomResponse(
        #       message="Burrobot says:", data=answer
        #   ).success()
