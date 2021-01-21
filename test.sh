gsutil cp core-site.xml gs://xml-to-json/
gsutil ls gs://xml-to-json/
gcloud functions logs read gcs_xml_to_json
