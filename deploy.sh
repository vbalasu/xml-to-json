gcloud functions deploy gcs_xml_to_json \
--runtime python38 \
--trigger-resource xml-to-json \
--trigger-event google.storage.object.finalize
