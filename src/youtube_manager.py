import datetime
import socket    
import pickle
import os

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


socket.setdefaulttimeout(100000)


class Youtube_Manager:
    def upload(self, video_data):
        CLIENT_SECRET_FILE = 'google_secret.json'
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

        service = self.create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        upload_date_time = (datetime.datetime.now() + datetime.timedelta(hours=2)).isoformat() + '.000Z'

        print(video_data)
        print(video_data["title"])

        request_body = {
            'snippet': {
                'categoryI': 23,
                'title': video_data['title'],
                'description': video_data['title'],
                'tags': ['Reddit', 'Funny', 'PewDiePie', 'Meme', 'Compilation', 'Beast']
            },
            'status': {
                'privacyStatus': 'private',
                # 'publishAt': upload_date_time,
                'selfDeclaredMadeForKids': False, 
            },
            'notifySubscribers': True
        }

        mediaFile = MediaFileUpload(video_data['video_name'])

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()


        service.thumbnails().set(
            videoId=response_upload.get('id'),
            media_body=MediaFileUpload(video_data['thumbnail'])
        ).execute()
    
    def create_service(self, client_secret_file, api_name, api_version, *scopes):
        CLIENT_SECRET_FILE = client_secret_file
        API_SERVICE_NAME = api_name
        API_VERSION = api_version
        SCOPES = [scope for scope in scopes[0]]

        cred = None

        pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

        if os.path.exists(pickle_file):
            with open(pickle_file, 'rb') as token:
                cred = pickle.load(token)

        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                cred = flow.run_local_server()

            with open(pickle_file, 'wb') as token:
                pickle.dump(cred, token)

        try:
            service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
            return service
        except Exception as e:
            return None

youtube_manager = Youtube_Manager()