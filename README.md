<div align="center">
  <a href="https://www.trainml.ai/"><img src="https://www.trainml.ai/static/img/trainML-logo-purple.png"></a><br>
</div>

# Regional Endpoint Example

### Prerequisites

Before beginning this example, ensure that you have satisfied the following prerequisites.

- A valid [trainML account](https://auth.trainml.ai/login?response_type=code&client_id=536hafr05s8qj3ihgf707on4aq&redirect_uri=https://app.trainml.ai/auth/callback) with a non-zero [credit balance](https://docs.trainml.ai/reference/billing-credits/)
- A python virtual environment with the [trainML CLI/SDK](https://github.com/trainML/trainml-cli) installed and [configured](https://docs.trainml.ai/reference/cli-sdk#authentication).
- At least one GPU system onboarded with [CloudBender™](https://docs.trainml.ai/reference/cloudbender/)
- A Regional Port Reservation configured in the same region as the CloudBender GPU system.

## Create the trainML Endpoint

To create the endpoint, run the following command from a python virtual environment with the [trainML CLI/SDK](https://github.com/trainML/trainml-cli) installed and [configured](https://docs.trainml.ai/reference/cli-sdk#authentication)

```
python create_endpoint.py RESERVATION_ID PORT
```

where `RESERVATION_ID` is the ID of the regional port reservation that the endpoint will listen on and `PORT` is the port number of the port reservation.
