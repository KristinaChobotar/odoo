# -*- coding: utf-8 -*-
from odoo import models, fields
import requests

class NewPost(models.Model):
    _name='new.post'


    name_sender=fields.Char(string='Ім\'я відправника')
    adress_sender=fields.Char(string='Адреса відправника')
    name_recipient=fields.Char(string='Ім\'я одержувача')
    adress_recipient=fields.Char(string='Адреса одержувача')
    form_of_payment=fields.Selection([('cash','Готівка'),('card','Карта')], string='Форма платежу', track_visibility='always')
    cost=fields.Integer(string='Вартість')

class NewPostUpdate(models.Model):
    _name = 'update.new.post'

    
    def _update_departments(self):
        # api_url = "https://api.novaposhta.ua/v2.0/json/"
        api_key = "74317ff685f9b1159e42fb8548074ebf"

        cities_payload = {
            "apiKey": "74317ff685f9b1159e42fb8548074ebf",
            "modelName": "Address",
            "calledMethod": "getCities",
            "methodProperties": {}
        }
        cities_response = requests.post("https://api.novaposhta.ua/v2.0/json/", json=cities_payload, headers={'Connection':'close'})

        if cities_response.status_code == 200:
            cities_data = cities_response.json().get('data', [])
            #TODO додати додавання міста в модель new.post.cities

            for city in cities_data:
                departments_payload = {
                    "apiKey": api_key,
                    "modelName": "AddressGeneral",
                    "calledMethod": "getWarehouses",
                    "methodProperties": {
                        "CityRef": city['Ref']
                    }
                }
                departments_response = requests.post("https://api.novaposhta.ua/v2.0/json/", json=departments_payload, headers={'Connection':'close'})

                if departments_response.status_code == 200:
                    departments_data = departments_response.json().get('data', [])

                    for department in departments_data:
                        department_vals = {
                            'site_key': department['SiteKey'],
                            'description': department['Description'],
                            'type_of_warehouse': department['TypeOfWarehouse'],
                            'ref': department['Ref'],
                            'city_ref': department['CityRef'],
                            'city_description': city['Description'],
                            'settlement_ref': department['Ref'],
                            'settlement_description': department['Description'],
                            'longitude': department['Longitude'],
                            'latitude': department['Latitude']
                        }

                        existing_department = self.env['new.post.department'].search([('ref', '=', department['Ref'])])
                        if existing_department:
                            existing_department.write(department_vals)
                        else:
                            self.env['new.post.department'].create(department_vals)

class NewPostDepartment(models.Model):
    _name = 'new.post.department'

# SiteKey:179
# Description:Відділення №1: вул. Руська, 248о
# TypeOfWarehouse:9a68df70-0267-42a8-bb5c-37f427e36ee4
# Ref:47402ec4-e1c2-11e3-8c4a-0050568002cf
# CityRef:e221d642-391c-11dd-90d9-001a92567626
# CityDescription:Чернівці
# SettlementRef:e71fe717-4b33-11e4-ab6d-005056801329
# SettlementDescription:Чернівці
# Longitude:25.989604000000000
# Latitude:48.272865000000000

    site_key = fields.Char(string='SiteKey')
    description = fields.Char(string='Description')
    type_of_warehouse = fields.Char(string='TypeOfWarehouse')
    ref = fields.Char(string='Ref')
    city_ref = fields.Char(string='CityRef')
    city_description = fields.Char(string='CityDescription')
    settlement_ref = fields.Char(string='SettlementRef')
    settlement_description = fields.Char(string='SettlementDescription')
    longitude = fields.Float(string='Longitude')
    latitude = fields.Float(string='Latitude')

class NewPostCities(models.Model):
    _name = 'new.post.cities'   

    # Description: Яцьківка
    # Ref: af4a63a9-7301-11e9-898c-005056b24375
    # Area:7150812c-9b87-11de-822f-000c2965ae0e
    # SettlementType:563ced13-f210-11e3-8c4a-0050568002cf
    # CityID:1712
    # SettlementTypeDescription:село
    # AreaDescription:Донецька

    description = fields.Char(string='Description')
    ref = fields.Char(string='Ref')
    area = fields.Char(string='Area')
    settlement_type = fields.Char(string='Settlement Type')
    city_id = fields.Integer(string='City ID')
    settlement_type_description = fields.Char(string='Settlement Type Description')
    area_description = fields.Char(string='Area Description')