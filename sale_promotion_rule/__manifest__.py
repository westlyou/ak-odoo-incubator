# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com)
# Benoît GUILLOT <benoit.guillot@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Promotion Rule",
    "summary": "Module to manage promotion rule on sale order",
    "version": "10.0.1.0.0",
    "category": "Sale",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale",
    ],
    "data": [
        'wizards/sale_order_add_coupon.xml',
        'views/sale_order.xml',
        'views/sale_promotion_rule.xml',
        'security/ir.model.access.csv',
    ],
    "qweb": [
    ]
}
