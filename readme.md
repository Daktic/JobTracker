# Hello
## This is a fun little tool to help keep track of job applications.
It may grow with time if I feel like adding to it, but it mainly just adds jobs to a Google sheet.

### Pre-requisites
- [Enable Google Workspace API](https://developers.google.com/workspace/guides/enable-apis)
    - Please note, this requires using Google Cloud. You will have to set up a payment method, even though the API is free.
- [Enable Google Sheet API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com)
### Setup
- [Create a service account](https://console.cloud.google.com/iam-admin/serviceaccounts/create)
  - I used the Editor role, though you could be more restrictive if you wish.
  - Create Service account Key
    - This should be a JSON
  - Add service account email to editor user list the Google Sheet you wish to use
  - Add the JSON file into the google_credentials folder