from flask import Flask, jsonify, abort
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from werkzeug.utils import secure_filename
import werkzeug
import os

app = Flask(__name__)
api = Api(app)
CORS(app, origins='http://127.0.0.1:5000')


app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CORS_HEADERS'] = 'Content-Type'

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the Video", required = True)
video_put_args.add_argument("likes", type=int, help="Likes for this Video", required = True)
video_put_args.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files', help="File for this Video", required = True)

videos = {}



def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404)




class Video(Resource):

    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def post(self, video_id):
        args = video_put_args.parse_args()
        print(args)
        name = args['name']
        likes = args['likes']
        file = args['file']

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        videos[video_id] = {'name': name,
                            'likes': likes,
                            'file': os.path.join(app.config['UPLOAD_FOLDER'], filename)}
        print(videos[video_id])
        return "Success!"
    




api.add_resource(Video, "/video/<int:video_id>")



if __name__ == "__main__":
    app.run(debug = True)