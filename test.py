from cgitb import text


a ={'object': 'whatsapp_business_account', 'entry': [{'id': '108615215310193', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550718328', 'phone_number_id': '111687571665026'}, 'contacts': [{'profile': {'name': '😊'}, 'wa_id': '263782953086'}], 'messages': [{'from': '263782953086', 'id': 'wamid.HBgMMjYzNzgyOTUzMDg2FQIAEhgUM0VCMEE2OEE0OUREMEJGQTY2M0UA', 'timestamp': '1661702895', 'text': {'body': 'hello'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
{"error":{"message":"Unsupported post request. Object with ID '111687571665026' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at https:\/\/developers.facebook.com\/docs\/graph-api","type":"GraphMethodException","code":100,"error_subcode":33,"fbtrace_id":"A5o2nzK-QPVA8BPgoKWiNwy"}}


b = a['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
ab =   []
for i in b:
    ab.append(i)
    #print(ab)

print(''.join(ab))