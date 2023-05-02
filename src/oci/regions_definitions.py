# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

REGIONS_SHORT_NAMES = {
    'yny': 'ap-chuncheon-1',
    'hyd': 'ap-hyderabad-1',
    'mel': 'ap-melbourne-1',
    'bom': 'ap-mumbai-1',
    'kix': 'ap-osaka-1',
    'icn': 'ap-seoul-1',
    'syd': 'ap-sydney-1',
    'nrt': 'ap-tokyo-1',
    'yul': 'ca-montreal-1',
    'yyz': 'ca-toronto-1',
    'ams': 'eu-amsterdam-1',
    'fra': 'eu-frankfurt-1',
    'zrh': 'eu-zurich-1',
    'jed': 'me-jeddah-1',
    'dxb': 'me-dubai-1',
    'gru': 'sa-saopaulo-1',
    'cwl': 'uk-cardiff-1',
    'lhr': 'uk-london-1',
    'iad': 'us-ashburn-1',
    'phx': 'us-phoenix-1',
    'sjc': 'us-sanjose-1',
    'vcp': 'sa-vinhedo-1',
    'scl': 'sa-santiago-1',
    'mtz': 'il-jerusalem-1',
    'mrs': 'eu-marseille-1',
    'sin': 'ap-singapore-1',
    'auh': 'me-abudhabi-1',
    'lin': 'eu-milan-1',
    'arn': 'eu-stockholm-1',
    'jnb': 'af-johannesburg-1',
    'cdg': 'eu-paris-1',
    'qro': 'mx-queretaro-1',
    'mad': 'eu-madrid-1',
    'ord': 'us-chicago-1',
    'lfi': 'us-langley-1',
    'luf': 'us-luke-1',
    'ric': 'us-gov-ashburn-1',
    'pia': 'us-gov-chicago-1',
    'tus': 'us-gov-phoenix-1',
    'ltn': 'uk-gov-london-1',
    'brs': 'uk-gov-cardiff-1',
    'nja': 'ap-chiyoda-1',
    'ukb': 'ap-ibaraki-1',
    'mct': 'me-dcc-muscat-1',
    'wga': 'ap-dcc-canberra-1',
    'bgy': 'eu-dcc-milan-1',
    'mxp': 'eu-dcc-milan-2',
    'snn': 'eu-dcc-dublin-2',
    'dtm': 'eu-dcc-rating-2',
    'dus': 'eu-dcc-rating-1',
    'ork': 'eu-dcc-dublin-1',
    'beg': 'eu-jovanovac-1'
}
REGION_REALMS = {
    'ap-chuncheon-1': 'oc1',
    'ap-hyderabad-1': 'oc1',
    'ap-melbourne-1': 'oc1',
    'ap-mumbai-1': 'oc1',
    'ap-osaka-1': 'oc1',
    'ap-seoul-1': 'oc1',
    'ap-sydney-1': 'oc1',
    'ap-tokyo-1': 'oc1',
    'ca-montreal-1': 'oc1',
    'ca-toronto-1': 'oc1',
    'eu-amsterdam-1': 'oc1',
    'eu-frankfurt-1': 'oc1',
    'eu-zurich-1': 'oc1',
    'me-jeddah-1': 'oc1',
    'me-dubai-1': 'oc1',
    'sa-saopaulo-1': 'oc1',
    'uk-cardiff-1': 'oc1',
    'uk-london-1': 'oc1',
    'us-ashburn-1': 'oc1',
    'us-phoenix-1': 'oc1',
    'us-sanjose-1': 'oc1',
    'sa-vinhedo-1': 'oc1',
    'sa-santiago-1': 'oc1',
    'il-jerusalem-1': 'oc1',
    'eu-marseille-1': 'oc1',
    'ap-singapore-1': 'oc1',
    'me-abudhabi-1': 'oc1',
    'eu-milan-1': 'oc1',
    'eu-stockholm-1': 'oc1',
    'af-johannesburg-1': 'oc1',
    'eu-paris-1': 'oc1',
    'mx-queretaro-1': 'oc1',
    'eu-madrid-1': 'oc1',
    'us-chicago-1': 'oc1',

    'us-langley-1': 'oc2',
    'us-luke-1': 'oc2',

    'us-gov-ashburn-1': 'oc3',
    'us-gov-chicago-1': 'oc3',
    'us-gov-phoenix-1': 'oc3',

    'uk-gov-london-1': 'oc4',
    'uk-gov-cardiff-1': 'oc4',

    'ap-chiyoda-1': 'oc8',
    'ap-ibaraki-1': 'oc8',

    'me-dcc-muscat-1': 'oc9',

    'ap-dcc-canberra-1': 'oc10',

    'eu-dcc-milan-1': 'oc14',
    'eu-dcc-milan-2': 'oc14',
    'eu-dcc-dublin-2': 'oc14',
    'eu-dcc-rating-2': 'oc14',
    'eu-dcc-rating-1': 'oc14',
    'eu-dcc-dublin-1': 'oc14',

    'eu-jovanovac-1': 'oc20'
}
REALMS = {
    'oc1': 'oraclecloud.com',
    'oc2': 'oraclegovcloud.com',
    'oc3': 'oraclegovcloud.com',
    'oc4': 'oraclegovcloud.uk',
    'oc8': 'oraclecloud8.com',
    'oc9': 'oraclecloud9.com',
    'oc10': 'oraclecloud10.com',
    'oc14': 'oraclecloud14.com',
    'oc20': 'oraclecloud20.com'
}
REGIONS = [
    'ap-chuncheon-1',
    'ap-hyderabad-1',
    'ap-melbourne-1',
    'ap-mumbai-1',
    'ap-osaka-1',
    'ap-seoul-1',
    'ap-sydney-1',
    'ap-tokyo-1',
    'ca-montreal-1',
    'ca-toronto-1',
    'eu-amsterdam-1',
    'eu-frankfurt-1',
    'eu-zurich-1',
    'me-jeddah-1',
    'me-dubai-1',
    'sa-saopaulo-1',
    'uk-cardiff-1',
    'uk-london-1',
    'us-ashburn-1',
    'us-phoenix-1',
    'us-sanjose-1',
    'sa-vinhedo-1',
    'sa-santiago-1',
    'il-jerusalem-1',
    'eu-marseille-1',
    'ap-singapore-1',
    'me-abudhabi-1',
    'eu-milan-1',
    'eu-stockholm-1',
    'af-johannesburg-1',
    'eu-paris-1',
    'mx-queretaro-1',
    'eu-madrid-1',
    'us-chicago-1',
    'us-langley-1',
    'us-luke-1',
    'us-gov-ashburn-1',
    'us-gov-chicago-1',
    'us-gov-phoenix-1',
    'uk-gov-london-1',
    'uk-gov-cardiff-1',
    'ap-chiyoda-1',
    'ap-ibaraki-1',
    'me-dcc-muscat-1',
    'ap-dcc-canberra-1',
    'eu-dcc-milan-1',
    'eu-dcc-milan-2',
    'eu-dcc-dublin-2',
    'eu-dcc-rating-2',
    'eu-dcc-rating-1',
    'eu-dcc-dublin-1',
    'eu-jovanovac-1'
]
