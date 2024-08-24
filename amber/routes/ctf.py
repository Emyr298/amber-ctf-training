from flask import Blueprint, request

ctf_bp = Blueprint("ctf", __name__)

@ctf_bp.route("/post-flags", methods=["POST"])
def post_flags():
    body = request.json
    return {
        "test": body
    }
