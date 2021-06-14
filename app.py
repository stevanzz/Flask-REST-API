from flask import Flask, jsonify, request
import requests
import json
from requests.exceptions import RequestException

app = Flask(__name__)

endpoint = 'https://jsonplaceholder.typicode.com/'


@app.route('/top-posts', methods=['GET'])
def top_posts():
    try:
        all_comments = query(endpoint + 'comments', 'GET')
        grouped_comments = {}
        for comment in all_comments:
            if comment['postId'] not in grouped_comments:
                grouped_comments[comment['postId']] = {
                    'total_number_of_comments': 1,
                    'post_id': comment['postId'],
                    'post_title': '',
                    'post_body': ''
                }
            else:
                grouped_comments[comment['postId']
                                 ]['total_number_of_comments'] += 1

        all_posts = query(endpoint + 'posts', 'GET')
        for post in all_posts:
            grouped_comments[post['id']]['post_title'] = post['title']
            grouped_comments[post['id']]['post_body'] = post['body']

        sorted_top_posts = sorted(grouped_comments.values(
        ), key=lambda x: x['total_number_of_comments'], reverse=True)

        return jsonify(sorted_top_posts)

    except RequestException as e:
        jsonify(e)


@app.route('/comments', methods=['GET'])
def comments():
    try:
        args = request.args
        all_comments = query(endpoint + 'comments', 'GET')
        for key, value in args.items():
            filtered_comments = []
            for comment in all_comments:
                if key not in comment:
                    return jsonify(error='Key "{}" not found'.format(key))

                if str(comment[key]) == str(value):
                    filtered_comments.append(comment)

            all_comments = filtered_comments

        return jsonify(all_comments)

    except RequestException as e:
        jsonify(e)


def query(url, method):
    if method == 'GET':
        response = requests.get(url)
        response.raise_for_status()
        return json.loads(response.text)
    elif method == 'POST':
        # TODO
        return None
    elif method == 'PUT':
        # TODO
        return None
    elif method == 'DELETE':
        # TODO
        return None


app.run(host='0.0.0.0', port=5000, debug=True)
