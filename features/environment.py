from behave import use_fixture
from allure_behave.hooks import allure_report
from base.fixtures import user


"""turn on fixture for each feature"""
def before_feature(context, feature):
    use_fixture(user, context)


allure_report("reports/")