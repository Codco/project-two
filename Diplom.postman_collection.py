{
	"info": {
		"_postman_id": "fea4171b-364f-4c32-8d12-685ded9b6f46",
		"name": "Diplom",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "19471945"
	},
	"item": [
		{
			"name": "users",
			"item": [
				{
					"name": "register user",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "email",
									"value": "prime-alfa@mail.ru",
									"description": "email адрес, будет использован для аутентификации (обязательное поле)",
									"type": "text"
								},
								{
									"key": "password",
									"value": "qwerty!@#$%",
									"description": "пароль (обязательное поле)",
									"type": "text"
								},
								{
									"key": "last_name",
									"value": "Ivanov",
									"description": "фамилия",
									"type": "text"
								},
								{
									"key": "first_name",
									"value": "Ivan",
									"description": "имя",
									"type": "text"
								},
								{
									"key": "patronymic",
									"value": "Ivanovich",
									"description": "отчество",
									"type": "text"
								},
								{
									"key": "company",
									"value": "House of Ivanov",
									"description": "компания",
									"type": "text"
								},
								{
									"key": "position",
									"value": "Manager",
									"description": "должность",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								""
							]
						},
						"description": "user registration"
					},
					"response": []
				},
				{
					"name": "confirm email [user activation]",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "uid",
									"value": "MTM",
									"description": "from the link sent to the email specified during registration .../activate/{uid}/{token}",
									"type": "text"
								},
								{
									"key": "token",
									"value": "b4ftlp-58bab6c00cfabb15a62c8e76241d69c8",
									"description": "from the link sent to the email specified during registration .../activate/{uid}/{token}",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/activation/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"activation",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "login user",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "email",
									"value": "uglin76@mail.ru",
									"type": "text"
								},
								{
									"key": "password",
									"value": "Horse4herO",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/token/login/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"token",
								"login",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "get user details",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token f078d75b38b30d025f2f3602f5f362ad4ce59037",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/me",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"me"
							]
						}
					},
					"response": []
				},
				{
					"name": "edit user deatails",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "last_name",
									"value": "Uglin",
									"type": "text"
								},
								{
									"key": "first_name",
									"value": "Alexsander",
									"type": "text"
								},
								{
									"key": "patronymic",
									"value": "",
									"type": "text"
								},
								{
									"key": "company",
									"value": "Alfa",
									"type": "text"
								},
								{
									"key": "position",
									"value": "Owner",
									"type": "text"
								},
								{
									"key": "type",
									"value": "shop",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/me/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"me",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "change user password",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "new_password",
									"value": "qwerty!@#$%",
									"type": "text"
								},
								{
									"key": "current_password",
									"value": "Horse4herO",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/set_password/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"set_password",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "reset user password",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "email",
									"value": "uglin76@mail.ru",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/reset_password/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"reset_password",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "reset password confirmation",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "uid",
									"value": "MQ",
									"description": "from link  .../activate/password/confirm/{uid}/{token}",
									"type": "text"
								},
								{
									"key": "token",
									"value": "b4jgpa-76be664849aa8dffe5fcb1aa9e2347ff",
									"description": "from link  .../activate/password/confirm/{uid}/{token}",
									"type": "text"
								},
								{
									"key": "new_password",
									"value": "Horse4herO",
									"description": "new password",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/users/reset_password_confirm/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"users",
								"reset_password_confirm",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "user logout",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/token/logout/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"token",
								"logout",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "user contacts",
			"item": [
				{
					"name": "get user contacts",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/user/contact/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"user",
								"contact",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "create user contact",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "person",
									"value": "Gorge Flint ",
									"type": "text"
								},
								{
									"key": "city",
									"value": "Washington",
									"type": "text"
								},
								{
									"key": "street",
									"value": "Pensilvania",
									"type": "text"
								},
								{
									"key": "house",
									"value": "222",
									"type": "text"
								},
								{
									"key": "apartment",
									"value": "",
									"type": "text"
								},
								{
									"key": "phone",
									"value": "+79813027735",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/user/contact/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"user",
								"contact",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "edit user contact",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "id",
									"value": "3",
									"type": "text"
								},
								{
									"key": "person",
									"value": "Max Payne",
									"type": "text"
								},
								{
									"key": "phone",
									"value": "+79210000000",
									"type": "text"
								},
								{
									"key": "city",
									"value": "New York",
									"type": "text"
								},
								{
									"key": "street",
									"value": "Broadway",
									"type": "text"
								},
								{
									"key": "house",
									"value": "245",
									"type": "text"
								},
								{
									"key": "building",
									"value": "1",
									"type": "text"
								},
								{
									"key": "apartment",
									"value": "45",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/user/contact/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"user",
								"contact",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "delete user contact",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "items",
									"value": "1,3",
									"description": "contact id",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/user/contact/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"user",
								"contact",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "partner",
			"item": [
				{
					"name": "get status",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "url",
									"value": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml",
									"type": "text"
								},
								{
									"key": "state",
									"value": "off",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/partner/state/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"partner",
								"state",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "change status",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "state",
									"value": "on",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/partner/state/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"partner",
								"state",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "update price",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "url",
									"value": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/partner/update/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"partner",
								"update",
								""
							],
							"query": [
								{
									"key": "",
									"value": null,
									"disabled": true
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "list orders",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "url",
									"value": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/partner/orders/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"partner",
								"orders",
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "shop",
			"item": [
				{
					"name": "list shops",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/shops/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"shops",
								""
							],
							"query": [
								{
									"key": "search",
									"value": "М-Видео",
									"description": "search by name",
									"disabled": true
								},
								{
									"key": "ordering",
									"value": "name",
									"description": "order by name or id",
									"disabled": true
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "list categories",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/categories",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"categories"
							]
						}
					},
					"response": []
				},
				{
					"name": "search products",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/product?category_id=15&shop_id=21",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"product"
							],
							"query": [
								{
									"key": "category_id",
									"value": "15"
								},
								{
									"key": "shop_id",
									"value": "21"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "add products in basket",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "items",
									"value": "[{ \"product_info\": 614, \"quantity\": 12 }, { \"product_info\": 615, \"quantity\": 12 }, { \"product_info\": 616, \"quantity\": 12 }]",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/basket/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"basket",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "edit product quantity in basket",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "items",
									"value": "[{ \"product_info\": 614, \"quantity\": 999 }, { \"product_info\": 615, \"quantity\": 999 }, { \"product_info\": 616, \"quantity\": 999 }, { \"product_info\": 619, \"quantity\": 12 }, { \"product_info\": 1616, \"quantity\": 12 }]",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/basket/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"basket",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "delete from basket",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "items",
									"value": "614,   615,    6add",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/basket/?",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"basket",
								""
							],
							"query": [
								{
									"key": "",
									"value": null
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "get basket content",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/basket/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"basket",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "list my orders",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "Token b5d1d663e993a1f826aa43b5ebfb280824ec021e",
								"type": "text"
							}
						],
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/orders",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"orders"
							]
						}
					},
					"response": []
				},
				{
					"name": "place order",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Token 7ad8fc7ae3a36f8c4a05fce375ea17fddc351c52",
								"type": "text"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "contact",
									"value": "11",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "http://127.0.0.1:8000/api/v1/orders/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"api",
								"v1",
								"orders",
								""
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
