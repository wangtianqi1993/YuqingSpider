# coding:utf-8
SearchNames = {
    'baidu': '百度新闻',
    'rqxx': '华油论坛',
    'hc360': '慧聪论坛',
    'kdnet': '凯迪论坛',
    'zhongsou': '中搜论坛',
    'tianya': '天涯论坛',
    'sunpetro': '阳光石油论坛',
    'oilhb': '华北油田论坛',
    'hcbbs': '海川论坛',
    '29nh': '东油论坛',
    'oilequipcn': '洛克斯石油论坛',
    'fracchina': '中国压裂网',
    'hg707': '化工707论坛',
    'mahoupao': '马后炮化工论坛',
    'jhyta': '江汉论坛',
    'petroren': '石油人论坛',
    'baiduyun': '百度云论坛',
    'daxues': '大学生网论坛',
    'mhg114': '煤化工114论坛',
    'bucter': '北化人论坛',
    'youqiyunshu': '油气运输论坛',
    'myubbs': '中国石油大学论坛',
    'oilsir': '中国石油先生论坛',
    'ltaaa': '龙腾网论坛',
    'hainei': '海内论坛',
    'rednet': '红网论坛',
    'cnr': '央广社区',
    'm4': '四月论坛',
    'haiwainet': '唐人街社区',
    'scol': '天府社区',
    'yinxiangzg': '印象社区',
    'gmw': '光明网论坛',
    'fyjs': '飞扬军事',
    '23zhibo': '爱上直播军事',
    'wj1818': '网聚战友社区',
    'lzszg': '龙之声论坛',
    'onefx': '汇客外汇论坛',
    'wacai': '挖财社区',
    '55168': '55168论坛',
    'fxunion': '外汇联盟论坛',
    'bi22': '比爱外汇论坛',
    'ruoshui': '若水股票论坛',
    '178448': '股海明灯论坛',
    'gupiao168': '股民大家庭论坛',
    'dqdaily': '大庆论坛',
    '010': '北京论坛',
}

SearchNameNew = {
    'baidu': '百度新闻',
    'qihoo': '360新闻',
    'youdao': '有道新闻',
    'sogou': '搜狗新闻',
    'sogoublog':'搜狗博客',
    'weibosearch':'新浪微博',
    'weibocontent':'新浪微博',
    'weibohot':'新浪微博',
    'petroren': '石油人论坛',
    'baiduyun': '百度云论坛',
    'daxues': '大学生网论坛',
    # 'sunpetro': '阳光石油论坛',
}

if __name__ == "__main__":
    a = {}
    a[1] = {}
    a[1][3] = 1
    if not 2 in a.keys() and not 4 in a[1].keys():
        print 'yes'
