#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import urllib3
import requests
import json

iam_token = "eyJraWQiOiIyMDIwMDgyMzE4MzIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMDdITVk5IiwiaWQiOiJJQk1pZC01NTAwMDdITVk5IiwicmVhbG1pZCI6IklCTWlkIiwiaWRlbnRpZmllciI6IjU1MDAwN0hNWTkiLCJnaXZlbl9uYW1lIjoiSHlva2lsIiwiZmFtaWx5X25hbWUiOiJLaW0iLCJuYW1lIjoiSHlva2lsIEtpbSIsImVtYWlsIjoiaGtpbUBib3V5Z3Vlc3RlbGVjb20uZnIiLCJzdWIiOiJoa2ltQGJvdXlndWVzdGVsZWNvbS5mciIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImFhNjNiZWJiYjkwYTQ0NDU5NmQ1OTFmYmUzMGY2ZTBjIiwiaW1zX3VzZXJfaWQiOiI4MzI4OTI2IiwiZnJvemVuIjp0cnVlLCJpbXMiOiIyMDA1OTk0In0sImlhdCI6MTU5ODUxODg1MSwiZXhwIjoxNTk4NTIyNDUxLCJpc3MiOiJodHRwczovL2lhbS5ibHVlbWl4Lm5ldC9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.JPujTYVamXwnAK_pGaU_E3kE-o9Y_tWYteX3zsGT2kr18CuyslXgD0feJHfRmKglsZa_KUaxjDSz13uL4zamGJ003rDqKArqfagO3Bi4itzRQhmvzjwHnbOor6PY2qwz6mXIowpi5TbDt0Sw70rMWQ0yD2hB-eY2px4AGApjCnrrMxNnYT4dkw_osYieY30VbrJLVuE_2vHmpvmC7pW1KTI4jOn3jL931WG5AZkIkpOA9ajXY4ROGHJnpkCDZyuQePWWz5RlDZNj6s-yZUT-sMzDWDREB6TVpXFAobTGN_bYHgaxYY0nu0Ve4Be0l_kyzPnDS_624JIhfTFaAY7a2w"
ml_instance_id = "6d21aeda-1dba-4536-a408-83b0fa2fb9c1"


def main(dict):
    print(dict)
    # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
    header = {'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

    if dict["user_has_outgoing_calls"] == "Oui":
        dict["user_has_outgoing_calls"] = 1
    elif dict["user_has_outgoing_calls"] == "Non":
        dict["user_has_outgoing_calls"] = 0

    if dict["user_has_outgoing_sms"] == "Oui":
        dict["user_has_outgoing_sms"] = 1
    elif dict["user_has_outgoing_sms"] == "Non":
        dict["user_has_outgoing_sms"] = 0

    if dict["user_use_gprs"] == "Oui":
        dict["user_use_gprs"] = 1
    elif dict["user_use_gprs"] == "Non":
        dict["user_use_gprs"] = 0

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"fields": ["user_spendings", "user_has_outgoing_calls", "user_has_outgoing_sms", "user_use_gprs", "calls_outgoing_to_abroad_spendings", "gprs_usage"],
                       "values": [[dict["user_spendings"], dict["user_has_outgoing_calls"], dict["user_has_outgoing_sms"], dict["user_use_gprs"], dict["calls_outgoing_to_abroad_spendings"], dict["gprs_usage"]]]}
    response_scoring = requests.post(
        'https://eu-de.ml.cloud.ibm.com/v3/wml_instances/6d21aeda-1dba-4536-a408-83b0fa2fb9c1/deployments/8804624d-50b8-42fa-8186-b7a3ec276b12/online', json=payload_scoring, headers=header)

    # print("Scoring response")
    response = json.loads(response_scoring.text)
    print(response)

    url = ""
    cluster = response["values"][0][0]

    # print(response)
    # print(response["values"][0][0])
    if response["values"][0][0] == "cluster-1":
        url = "https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement/sensation/sim-seule-100mo"
    elif response["values"][0][0] == "cluster-2":
        url = "https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement/sensation/sim-seule-40mo"
    elif response["values"][0][0] == "cluster-3":
        url = "https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement/sensation/sim-seule-50go"
    elif response["values"][0][0] == "cluster-4":
        url = "https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement/sensation/sim-seule-50go"
    elif response["values"][0][0] == "cluster-5":
        url = "https://www.bouyguestelecom.fr/forfaits-mobiles/avec-engagement/sensation/sim-seule-5go"

    return {'url': url, 'cluster': cluster}
