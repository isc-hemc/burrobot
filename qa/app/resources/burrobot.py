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

    def post(self) -> Response:
        """GET Request.

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

        if not payload:
            return CustomResponse(
                message="Empty Payload: JSON content expected."
            ).error()

        try:
            context_id, question = itemgetter("context_id", "question")(
                payload
            )
        except KeyError:
            return CustomResponse(
                message="context_id or question keys required."
            ).error()

        cms_api = os.environ.get("CMS_API_HOST")

        try:
            res = http_request.get(f"{cms_api}/context/{context_id}").json()
        except Exception:
            return CustomResponse(
                message="Unable to reach the CMS API."
            ).error(404)

        context = res["data"]["description"]

        answer = self.qa(context=context, question=question)

        return CustomResponse(message="Burrobot says:", data=answer).success()
