# coding: UTF-8
import settings
import tweepy
import numpy as np

#-----------------------------------------------------------------------------
# keyの指定(情報漏洩を防ぐため伏せています)
consumer_key = settings.CK
consumer_secret = settings.CS
access_token = settings.AT
access_token_secret = settings.ATC

# tweepyの設定（認証情報を設定）
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepyの設定（APIインスタンスの作成）
api = tweepy.API(auth)

#-----------------------------------------------------------------------------
###z = np.random.choice(['麻', '雀', '部', '設', '立', '部', '同', '好', '会'])
a = np.random.choice(['麻', '雀', '部'])
b = np.random.choice(['麻', '雀', '部'])
c = np.random.choice(['麻', '雀', '部'])
d = np.random.choice(['設', '立', '部'])
e = np.random.choice(['設', '立', '部'])
f = np.random.choice(['設', '立', '部'])
g = np.random.choice(['同', '好', '会'])
h = np.random.choice(['同', '好', '会'])
i = np.random.choice(['同', '好', '会'])

x = a + b + c + d + e + f + g + h + i + '(非公式)'
api.update_status(status = x)
