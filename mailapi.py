def email_entrypoint(
        lookback_time: int=5, credentials_path:str=""
):
    return [{
    "id": "18f58e845651f1fe",
    "threadId": "18f58e845651f1fe",
    "labelIds": [
        "UNREAD",
        "CATEGORY_UPDATES",
        "INBOX"
    ],
    "payload": {
        "partId": "",
        "headers": [
            {
                "name": "Delivered-To",
                "value": "ramachandran.aashiq@gmail.com"
            },
            {
                "name": "Received",
                "value": "by 2002:adf:f6ca:0:b0:34d:2618:f679 with SMTP id y10csp473084wrp;        Wed, 8 May 2024 08:52:48 -0700 (PDT)"
            },
            {
                "name": "X-Google-Smtp-Source",
                "value": "AGHT+IGeWNwToFDAbqprRc/oPauEb1jPf1/crZ9MBPF8zfnIv6u3dz5E+EzvmMjPgGXut72jYASm"
            },
            {
                "name": "X-Received",
                "value": "by 2002:a05:620a:4150:b0:792:a77f:fe71 with SMTP id af79cd13be357-792b26a8bffmr380932885a.2.1715183568124;        Wed, 08 May 2024 08:52:48 -0700 (PDT)"
            },
            {
                "name": "ARC-Seal",
                "value": "i=1; a=rsa-sha256; t=1715183568; cv=none;        d=google.com; s=arc-20160816;        b=Qda5gkMFqpMmqe40Ram9RXrdfEnfotYp7MdsytglcdKsg6awCpzzqaAtF9bJq1dxNf         BKIyZLu/WbIHAnmwWTyHNuO9I1xl8n6zdpm86i2mkPiD5ljLjMwdY4j28TzjnWcAtWaq         xNFKBJOngMFE3Y+EKcRXXXsMgAwhBxpZZn+cib5mrqf9t3tyvyd2NeN+cIzL8bD2qXwg         ugoc7gzmjrzpH9afi4PCzmBegGYC9TYcNA6pEV49BJwDrYhbgDgEZoR0sR2Kr7MNG3BY         jZFcf5Y312Ao9swpvewdEXzXdq3yEpfPV6ofN7q1DYcKTF2sByl3iRZXR1AIci8cOhMU         KSUg=="
            },
            {
                "name": "ARC-Message-Signature",
                "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=require-recipient-valid-since:feedback-id:list-unsubscribe-post         :list-unsubscribe:date:to:mime-version:subject:message-id:from         :dkim-signature:dkim-signature;        bh=PyAw2z2IGrw3KGh+r84yQN4rhMjhGY3YcCEPI6hR7I0=;        fh=pBSjOIYkeLuCjQCmkhKXtk384fd1QpXJK9CCW8AoFFc=;        b=N+Ux80u6kL2GnavbjsDoejWUxsvf/I3uNKY2i7cddmfOGzcMpI8/zKiiT3Nl6UECqp         4KItPwW948awmxI45rk7Z9QMVGztKnCSTQ7EwHY73jPZ635K3Vh9nIyb4i2w038OdxI9         dsysZS0sziMCVA5Mb0vomZPX+W+oOBzad3mQ3hoqRlCq3y3RZJxzAJQLW5tfEFYtHiFi         rhvf3PsvUDBKt4yjChAZym2tTphxxL6h3qBI9MFJtUpTBqP3OjuKwDbEkDzM7I6KAoNM         +guYaF0+LwuCZAHmpQLyZs992l8ioVKlihx9UOea5JhgLRshiheGTGs5vL/5vIFGWVfj         LzZA==;        dara=google.com"
            },
            {
                "name": "ARC-Authentication-Results",
                "value": "i=1; mx.google.com;       dkim=pass header.i=@maild.linkedin.com header.s=d2048-202308-0d header.b=Y4gOXssV;       dkim=pass header.i=@linkedin.com header.s=d2048-202308-00 header.b=lhafs1Jd;       spf=pass (google.com: domain of s-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com designates 108.174.0.188 as permitted sender) smtp.mailfrom=s-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=linkedin.com"
            },
            {
                "name": "Return-Path",
                "value": "\u003cs-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com\u003e"
            },
            {
                "name": "Received",
                "value": "from maild-hd.linkedin.com (maild-hd.linkedin.com. [108.174.0.188])        by mx.google.com with ESMTPS id xy25-20020a05620a5dd900b0078ee090d0f3si13536536qkn.632.2024.05.08.08.52.47        for \u003cramachandran.aashiq@gmail.com\u003e        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Wed, 08 May 2024 08:52:48 -0700 (PDT)"
            },
            {
                "name": "Received-SPF",
                "value": "pass (google.com: domain of s-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com designates 108.174.0.188 as permitted sender) client-ip=108.174.0.188;"
            },
            {
                "name": "Authentication-Results",
                "value": "mx.google.com;       dkim=pass header.i=@maild.linkedin.com header.s=d2048-202308-0d header.b=Y4gOXssV;       dkim=pass header.i=@linkedin.com header.s=d2048-202308-00 header.b=lhafs1Jd;       spf=pass (google.com: domain of s-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com designates 108.174.0.188 as permitted sender) smtp.mailfrom=s-4vluffkkvfu3clt0wik2ohmst67xmxizhh27iuz2e4z94qgdh5i6mxr6@bounce.linkedin.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=linkedin.com"
            },
            {
                "name": "DKIM-Signature",
                "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=maild.linkedin.com; s=d2048-202308-0d; t=1715183562; bh=PyAw2z2IGrw3KGh+r84yQN4rhMjhGY3YcCEPI6hR7I0=; h=From:Subject:MIME-Version:Content-Type:To:Date:X-LinkedIn-Class:\t X-LinkedIn-Template:X-LinkedIn-fbl; b=Y4gOXssVKK/FkcTZVQwbH0XGXF+cSJvcAOKoIM2tu2CqaimL4GqcvGnRpmnQm8oa5\t JAI2Y7iOCjZ3QlNTt405fUjF5442wbkUBAxAIOC5jNJe/gA2GKRPIw3PizF6n3VQzI\t IxBdzATroviOT2mIXT3geeYG7oPyukD7Bb7OJBYyoLYanzxldvcErcqjV824AzPxwb\t JgnaKKAmt0ix87xyD5X8x2j9z4X1ezc34zFQ7eqLGheiFNc3dl2oc8U/G6y7iyFrA7\t ekf9hqnIfXUsiAQFMvDS7Cytp2s+RHvuK+Wfy0xLRUn+8dtQWQp/uKRnRmkhmzFzCv\t 8bDu6fiSoKhHA=="
            },
            {
                "name": "DKIM-Signature",
                "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=linkedin.com; s=d2048-202308-00; t=1715183562; bh=PyAw2z2IGrw3KGh+r84yQN4rhMjhGY3YcCEPI6hR7I0=; h=From:Subject:MIME-Version:Content-Type:To:Date:X-LinkedIn-Class:\t X-LinkedIn-Template:X-LinkedIn-fbl; b=lhafs1JdKUdcspXXDC0XPcwsxa+alUdsuglqimREkU7iKodZX96sTrty04Vo2aRwH\t nwe8KTFVV1h2o+K6wQgde40Ye02ZBp77Louu8vSi6cUVKNmob+TNgyBrYpKKo2tVT1\t LtiqWM8yS4kLTCre1qdEPyHtAotsZZkEUAzYFvTdtCXV8RCi3nuDOCVIpPnnbfmIkU\t uCp+CC7YodarGGYocbuUxIdFNXbla9N5h82Ylu6xFzN840kj8iHvJ2CZ/agWRnDQlk\t wfGEiCFojYO2rSSjt+uFWB7ubvZa/yZA8/hbVHWU0b2XNgQdUI7ZpQGyRbZBvBj0fu\t kLB2mUAixoaig=="
            },
            {
                "name": "From",
                "value": "LinkedIn Job Alerts \u003cjobalerts-noreply@linkedin.com\u003e"
            },
            {
                "name": "Message-ID",
                "value": "\u003c2060193629.3952962.1715183562225@lva1-app99163.prod.linkedin.com\u003e"
            },
            {
                "name": "Subject",
                "value": "Sign in Alert"
            },
            {
                "name": "MIME-Version",
                "value": "1.0"
            },
            {
                "name": "Content-Type",
                "value": "multipart/alternative; boundary=\"----=_Part_3952960_908236983.1715183562221\""
            },
            {
                "name": "To",
                "value": "Aashiq Ramachandran \u003cramachandran.aashiq@gmail.com\u003e"
            },
            {
                "name": "Date",
                "value": "Wed, 8 May 2024 15:52:42 +0000 (UTC)"
            },
            {
                "name": "X-LinkedIn-Class",
                "value": "SAVEDSEARCH"
            },
            {
                "name": "X-LinkedIn-Template",
                "value": "email_job_alert_digest_01"
            },
            {
                "name": "X-LinkedIn-fbl",
                "value": "m2-clvfng4hstwb41e2lnslnsbrz6pigp712861jox86c0dcnrwiyyirkekzdspd38r0y6i9nn4unt4tc0isrgen805uiczv3nike5yfhlo7eas77ugdqhzuahwhoefw1xzshcdrghl"
            },
            {
                "name": "X-LinkedIn-Id",
                "value": "ct2tcb-lvxymfd9-ib"
            },
            {
                "name": "List-Unsubscribe",
                "value": "\u003chttps://www.linkedin.com/job-alert-email-unsubscribe?savedSearchId=1729700669&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BH%2BHXfHEsRKCTKZ25gNGmKA%3D%3D&midToken=AQHxozcL9cc_Zg&midSig=0rm062l2qocrg1&ek=email_job_alert_digest_01&e=ct2tcb-lvxymfd9-ib&eid=ct2tcb-lvxymfd9-ib&m=unsub&ts=unsub&li=0&t=plh\u003e"
            },
            {
                "name": "List-Unsubscribe-Post",
                "value": "List-Unsubscribe=One-Click"
            },
            {
                "name": "Feedback-ID",
                "value": "email_job_alert_digest_01:linkedin"
            },
            {
                "name": "Require-Recipient-Valid-Since",
                "value": "ramachandran.aashiq@gmail.com; Sat, 9 Nov 2019 05:12:38 +0000"
            }
        ]
    },
    "sizeEstimate": 174440,
    "historyId": "8474550",
    "internalDate": "1715183562000"
}]