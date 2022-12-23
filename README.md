# weatherES
Simple python script to get your local weather and ship it to an Elasticsearch cluster. Uses the openweather API so you'll need to sign up for an account to generate an API key. Additionally the script is written for connecting to an Elastic Cloud deployment rather than a local cluster.

Built to run for a defined time (one hour by default) and execute every five minutes, shipping the current weather conditions to the cluster. Great for getting some relevant test data to search and visualize on in Elasticsearch.

You'll need to grab the Elasticsearch python module, pytz, and requests from pip for this to work.
