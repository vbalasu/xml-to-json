def xml_to_json(xml_string):
    import xmltodict, json
    data = xmltodict.parse(xml_string)
    return json.dumps(data)

def gcs_xml_to_json(event, context):
    print('Event: ', event)
    print('Context: ', context)
    name = event['name']
    if name[-4:] == '.xml':
        import os
        # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/vbalasubramaniam/google/dataprep-premium-demo-aca864fa33dc.json'
        from google.cloud import storage
        storage_client = storage.Client()
        bucket = storage_client.bucket('xml-to-json')
        xml_blob = bucket.blob(event['name'])
        json_blob = bucket.blob(event['name'].replace('.xml', '.json'))
        json_blob.upload_from_string(xml_to_json(xml_blob.download_as_string()))
        print(f'Wrote to gs://xml-to-json/{json_blob}')