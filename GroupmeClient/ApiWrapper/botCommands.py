from .command import Command


class Post(Command):
    ''' Post a message from a bot
        HTTP POST
        Params
        bot_id *: string
        text *: string
        picture_url : string
    '''

    ##201 expected response code

    def __init__(self, botidAccessToken, text=None, picture_url=None, **kwargs):
        self.args = kwargs
        self.text = text
        self.picture_url = picture_url
        super(Post, self).__init__(botidAccessToken, 'POST')

    def createUrl(self):
        return self.URL_BASE + '/bots' + '/post' + self.TOKEN_QUERY_STRING

    def createLoad(self):
        load = {}
        if self.text is not None:
            load['text'] = self.text
        if self.picture_url is not None:
            load['picture_url'] = self.picture_url
        return load

    def makeCall(self):
        return super(Post, self).makeCall()