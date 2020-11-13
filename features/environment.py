from behave import use_fixture
from base.fixtures import user
from allure_behave.hooks import allure_report


"""turn on fixture for each feature"""
def before_feature(context, feature):
    context.bot = feature.tags
    use_fixture(user, context)


"""create allure reports"""
allure_report("reports/")



