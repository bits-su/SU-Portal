# suportal

Student Union Portal

## Dev docs

To set up the dev env: `tools/setup`. This script will create the
virtualenv and install the required dependencies.

To set up the dev database: `tools/setup_db`. This script will
create a new database and a new mysql user for testing.

To activate the virtualenv: `source tools/activate`. You will need
to run this step in any new terminal session you start.

To deactivate the virtualenv: `deactivate`.

Also, whenever a new dependency is added to the `requirements.txt`
file, you will need to run `tools/setup` again.

## Discussion

~~We hang out on https://crux-bphc.slack.com stream #suportal.~~ That was for the initial development only. From now on, the main discussion would be via the issue tracker for needed features/bugs.
