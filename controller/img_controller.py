'''
view file list
'''
# -*- encoding utf-8 -*-
import os
from flask import Blueprint, current_app, render_template
from flask_login import login_required

APP = Blueprint("img_controller", __name__)

@APP.route("/img", methods=["POST", "GET"])
@login_required
def root():
    '''
    access dirctory
    '''
    path = os.environ["JPG_PATH"]
    #拡張子JPGのファイル一覧を取得
    file_names = filter(\
        lambda name: name.rsplit(".")[1] \
        == "JPG", sorted(os.listdir(path), reverse=True))

    img_objects = map(\
        lambda file_name: FileProperty(file_name, path + "/" + file_name),\
        file_names)


    current_app.logger.info(" veiw img files ")

    return render_template("img_list.html", img_list=img_objects)

class FileProperty:
    '''
    file property
    '''
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
