from TikTokApi import TikTokApi
#import pprint

verifyFp = "verify_ky9tpy72_FkyPAIFK_ccYe_4pWy_9pDY_KNR9C3Jux8CF"


api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoint=True)
#api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
#api = TikTokApi()
# username = 'cretivox'
#a = 10
tiktoks = api.trending()
print(tiktoks)
# tiktoks = TikTokApi.by_username(username, video)
#tiktoks = api.byUsename(username, video)
#tiktoks = api.by_hashtag("fixie", count=a)
# tiktoks = api.by_trending(count=a, custom_verifyFp=verifyFp)
# print(tiktoks)
#for tiktok in tiktoks:

#     print(tiktok)
