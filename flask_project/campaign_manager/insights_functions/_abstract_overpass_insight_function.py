__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '17/05/17'

from abc import ABCMeta
from campaign_manager.insights_functions._abstract_insights_function import (
    AbstractInsightsFunction
)

from campaign_manager.data_providers.overpass_provider import OverpassProvider


class AbstractOverpassInsightFunction(AbstractInsightsFunction):
    __metaclass__ = ABCMeta
    category = ['quality']
    FEATURES_MAPPING = {
        'buildings': 'building',
        'roads': 'road'
    }
    icon = 'list'
    _function_good_data = None  # cleaned data

    last_update = ''
    is_updating = False

    def initiate(self, additional_data):
        """ Initiate function

        :param additional_data: additional data that needed
        :type additional_data:dict
        """
        if self.feature in self.FEATURES_MAPPING:
            self.feature = self.FEATURES_MAPPING[self.feature]

    def get_data_from_provider(self):
        """ Get data provider function
        :return: data from provider
        :rtype: dict
        """
        overpass_data = OverpassProvider().get_data(
            self.feature,
            self.campaign.corrected_coordinates()
        )
        self.last_update = overpass_data['last_update']
        self.is_updating = overpass_data['updating_status']
        return overpass_data['features']
