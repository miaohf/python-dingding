import json

import requests

from dingding_api.base import DingBase


class DingMessage(DingBase):
    """
    钉钉消息相关api
    """
    def send_msg(self, msg, user_list, dept_list, agent_id='84604603', msg_type='text'):
        urls = self.base_url + 'message/send?access_token=' + self.token
        params = {
            # 'touser': user_list,
            # 'toparty': dept_list,
            'agentid': agent_id,
            'msgtype': msg_type,
            msg_type: {
                'content': msg,
            }
        }
        if user_list:
            params['touser'] = user_list
        if dept_list:
            params['toparty'] = dept_list
        params = json.dumps(params)
        r = requests.post(urls, params, headers=self.headers)
        data = json.loads(r.text, encoding="utf-8")
        return data

    def upload_media(self, image_obj, upload_type='image'):
        """
        上传媒体文件
        :param image_obj:
        :param upload_type:
        :return:
        """
        urls = self.base_url + 'media/upload?access_token={}&type={}'.format(self.token, upload_type)
        if isinstance(image_obj, str):
            params = {
                'media': open(image_obj, 'rb'),
            }
        else:
            params = {
                'media': image_obj,
            }
        r = requests.post(urls, files=params)
        data = json.loads(r.text, encoding="utf-8")
        return data

    def send_image(self, media_id, user_list, agent_id='84604603', msg_type='image'):
        urls = self.base_url + 'message/send?access_token=' + self.token
        params = {
            'touser': user_list,
            'agentid': agent_id,
            'msgtype': msg_type,
            msg_type: {
                "media_id": media_id,
            }
        }
        params = json.dumps(params)
        r = requests.post(urls, params, headers=self.headers)
        data = json.loads(r.text, encoding="utf-8")
        return data