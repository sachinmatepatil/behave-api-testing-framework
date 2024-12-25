from behave import given, when, then


@given('I have installed Behave')
def step_given_installed_behave(context):
    print("Behave is installed.")


@when('I run Behave')
def step_when_run_behave(context):
    print("Running behave tests..")


@then('I should see Behave execute successfully')
def step_then_execute_successfully(context):
    print("Behave execute successfully!")
