# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decrypt_tokyo.settings')
django.setup()

from idol_token.models import Idol, Idol_Item
from cloudinary import CloudinaryImage
import cloudinary, cloudinary.uploader, cloudinary.forms, cloudinary.api

if __name__ == '__main__':

    image='redhat_72px_34197_easyicon.net_crrkmb4.png'

    ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')

    print(ret)



    # idol = Idol.objects.create(
    #     name='田中ひよこ',
    #     image='redhat_72px_34197_easyicon.net_crrkmb4.png',
    #     address='1243567654ffdsadfsdf'
    # )
    # print(idol)
