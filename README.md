# weatherES
Simple python script to get your local weather and ship it to an Elasticsearch cluster. Uses the openweather API so you'll need to sign up for an account to generate an API key. Additionally the script is written for connecting to an Elastic Cloud deployment rather than a local cluster.

You'll need the Elasticsearch python module as well as the pytz module for getting the local time.