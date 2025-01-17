# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020, 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for ResourceControllerV2
"""

import os
import time
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.resource_controller_v2 import *

#
# This file provides an example of how to use the Resource Controller service.
#
# The following configuration properties are assumed to be defined:
#
# RESOURCE_CONTROLLER_URL=<service url>
# RESOURCE_CONTROLLER_AUTH_TYPE=iam
# RESOURCE_CONTROLLER_AUTH_URL=<IAM Token Service url>
# RESOURCE_CONTROLLER_APIKEY=<User's IAM API Key>
# RESOURCE_CONTROLLER_RESOURCE_GROUP=<Short ID of the user's resource group>
# RESOURCE_CONTROLLER_PLAN_ID=<Unique ID of the plan associated with the offering>
# RESOURCE_CONTROLLER_ACCOUNT_ID=<User's account ID>
# RESOURCE_CONTROLLER_ALIAS_TARGET_CRN=<The CRN of target name(space) in a specific environment>
# RESOURCE_CONTROLLER_BINDING_TARGET_CRN=<The CRN of application to bind to in a specific environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'resource_controller.env'

resource_controller_service = None

config = None

instance_guid = None
alias_guid = None
binding_guid = None
instance_key_guid = None
resource_group = None
resource_plan_id = None
account_id = None
alias_target_crn = None
binding_target_crn = None
reclamation_id = None
resource_instance_name = 'RcSdkInstance1Python'
resource_instance_update_name = 'RcSdkInstanceUpdate1Python'
alias_name = 'RcSdkAlias1Python'
alias_update_name = 'RcSdkAliasUpdate1Python'
binding_name = 'RcSdkBinding1Python'
binding_update_name = 'RcSdkBindingUpdate1Python'
key_name = 'RcSdkKey1Python'
key_update_name = 'RcSdkKeyUpdate1Python'
target_region = 'global'

##############################################################################
# Start of Examples for Service: ResourceControllerV2
##############################################################################
# region


class TestResourceControllerV2Examples:
    """
    Example Test Class for ResourceControllerV2
    """

    @classmethod
    def setup_class(cls):
        global resource_controller_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            resource_controller_service = ResourceControllerV2.new_instance()

            # end-common
            assert resource_controller_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ResourceControllerV2.DEFAULT_SERVICE_NAME)

            global resource_group
            resource_group = config['RESOURCE_GROUP']

            global resource_plan_id
            resource_plan_id = config['RECLAMATION_PLAN_ID']

            global account_id
            account_id = config['ACCOUNT_ID']

            global alias_target_crn
            alias_target_crn = config['ALIAS_TARGET_CRN']

            global binding_target_crn
            binding_target_crn = config['BINDING_TARGET_CRN']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_resource_instance_example(self):
        """
        create_resource_instance request example
        """
        try:
            global instance_guid, resource_instance_name, target_region, resource_group, resource_plan_id
            print('\ncreate_resource_instance() result:')
            # begin-create_resource_instance

            resource_instance = resource_controller_service.create_resource_instance(
                name=resource_instance_name,
                target=target_region,
                resource_group=resource_group,
                resource_plan_id=resource_plan_id,
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-create_resource_instance

            instance_guid = resource_instance.get('guid')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_instance_example(self):
        """
        get_resource_instance request example
        """
        try:
            global instance_guid
            print('\nget_resource_instance() result:')
            # begin-get_resource_instance

            resource_instance = resource_controller_service.get_resource_instance(id=instance_guid).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-get_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_instances_example(self):
        """
        list_resource_instances request example
        """
        try:
            print('\nlist_resource_instances() result:')
            # begin-list_resource_instances

            all_results = []
            pager = ResourceInstancesPager(
                client=resource_controller_service,
                name=resource_instance_name,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_instances
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_instance_example(self):
        """
        update_resource_instance request example
        """
        try:
            global instance_guid, resource_instance_update_name
            print('\nupdate_resource_instance() result:')
            # begin-update_resource_instance

            parameters = {'exampleProperty': 'exampleValue'}
            resource_instance = resource_controller_service.update_resource_instance(
                id=instance_guid, name=resource_instance_update_name, parameters=parameters
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-update_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_alias_example(self):
        """
        create_resource_alias request example
        """
        try:
            global instance_guid, alias_name, alias_guid, alias_target_crn
            print('\ncreate_resource_alias() result:')
            # begin-create_resource_alias

            resource_alias = resource_controller_service.create_resource_alias(
                name=alias_name, source=instance_guid, target=alias_target_crn
            ).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-create_resource_alias

            alias_guid = resource_alias.get('guid')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_alias_example(self):
        """
        get_resource_alias request example
        """
        try:
            global alias_guid
            print('\nget_resource_alias() result:')
            # begin-get_resource_alias

            resource_alias = resource_controller_service.get_resource_alias(id=alias_guid).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-get_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_aliases_example(self):
        """
        list_resource_aliases request example
        """
        try:
            global alias_name
            print('\nlist_resource_aliases() result:')
            # begin-list_resource_aliases

            all_results = []
            pager = ResourceAliasesPager(
                client=resource_controller_service,
                name=alias_name,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_aliases
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_alias_example(self):
        """
        update_resource_alias request example
        """
        try:
            global alias_guid, alias_update_name
            print('\nupdate_resource_alias() result:')
            # begin-update_resource_alias

            resource_alias = resource_controller_service.update_resource_alias(
                id=alias_guid, name=alias_update_name
            ).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-update_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_aliases_for_instance_example(self):
        """
        list_resource_aliases_for_instance request example
        """
        try:
            global instance_guid
            print('\nlist_resource_aliases_for_instance() result:')
            # begin-list_resource_aliases_for_instance

            all_results = []
            pager = ResourceAliasesForInstancePager(
                client=resource_controller_service,
                id=instance_guid,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_aliases_for_instance
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_binding_example(self):
        """
        create_resource_binding request example
        """
        try:
            global alias_guid, binding_guid, binding_name, binding_target_crn
            print('\ncreate_resource_binding() result:')
            # begin-create_resource_binding

            parameters = {'exampleParameter': 'exampleValue'}
            resource_binding = resource_controller_service.create_resource_binding(
                source=alias_guid, target=binding_target_crn, name=binding_name, parameters=parameters
            ).get_result()

            print(json.dumps(resource_binding, indent=2))

            # end-create_resource_binding

            binding_guid = resource_binding.get('guid')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_binding_example(self):
        """
        get_resource_binding request example
        """
        try:
            global binding_guid
            print('\nget_resource_binding() result:')
            # begin-get_resource_binding

            resource_binding = resource_controller_service.get_resource_binding(id=binding_guid).get_result()
            if resource_binding.get('credentials') and resource_binding.get('credentials').get('REDACTED'):
                print(
                    "Credentials are redacted with code:",
                    resource_binding.get('credentials').get('REDACTED'),
                    ".The User doesn't have the correct access to view the credentials. Refer to the API documentation for additional details.",
                )
            print(json.dumps(resource_binding, indent=2))

            # end-get_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_bindings_example(self):
        """
        list_resource_bindings request example
        """
        try:
            global binding_name
            print('\nlist_resource_bindings() result:')
            # begin-list_resource_bindings

            all_results = []
            pager = ResourceBindingsPager(
                client=resource_controller_service,
                name=binding_name,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_bindings
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_binding_example(self):
        """
        update_resource_binding request example
        """
        try:
            global binding_guid, binding_update_name
            print('\nupdate_resource_binding() result:')
            # begin-update_resource_binding

            resource_binding = resource_controller_service.update_resource_binding(
                id=binding_guid, name=binding_update_name
            ).get_result()

            print(json.dumps(resource_binding, indent=2))

            # end-update_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_bindings_for_alias_example(self):
        """
        list_resource_bindings_for_alias request example
        """
        try:
            global alias_guid
            print('\nlist_resource_bindings_for_alias() result:')
            # begin-list_resource_bindings_for_alias

            all_results = []
            pager = ResourceBindingsForAliasPager(
                client=resource_controller_service,
                id=alias_guid,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_bindings_for_alias
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_key_example(self):
        """
        create_resource_key request example
        """
        try:
            global instance_guid, instance_key_guid, key_name
            print('\ncreate_resource_key() result:')
            # begin-create_resource_key

            parameters = {'exampleParameter': 'exampleValue'}
            resource_key = resource_controller_service.create_resource_key(
                name=key_name, source=instance_guid, parameters=parameters
            ).get_result()

            print(json.dumps(resource_key, indent=2))

            # end-create_resource_key

            instance_key_guid = resource_key.get('guid')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_key_example(self):
        """
        get_resource_key request example
        """
        try:
            global instance_key_guid
            print('\nget_resource_key() result:')
            # begin-get_resource_key

            resource_key = resource_controller_service.get_resource_key(id=instance_key_guid).get_result()
            if resource_key.get('credentials') and resource_key.get('credentials').get('REDACTED'):
                print(
                    "Credentials are redacted with code:",
                    resource_key.get('credentials').get('REDACTED'),
                    ".The User doesn't have the correct access to view the credentials. Refer to the API documentation for additional details.",
                )

            print(json.dumps(resource_key, indent=2))

            # end-get_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_keys_example(self):
        """
        list_resource_keys request example
        """
        try:
            global key_name
            print('\nlist_resource_keys() result:')
            # begin-list_resource_keys

            all_results = []
            pager = ResourceKeysPager(
                client=resource_controller_service,
                name=key_name,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_keys
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_key_example(self):
        """
        update_resource_key request example
        """
        try:
            global instance_key_guid, key_update_name
            print('\nupdate_resource_key() result:')
            # begin-update_resource_key

            resource_key = resource_controller_service.update_resource_key(
                id=instance_key_guid, name=key_update_name
            ).get_result()

            print(json.dumps(resource_key, indent=2))

            # end-update_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_keys_for_instance_example(self):
        """
        list_resource_keys_for_instance request example
        """
        try:
            global instance_guid
            print('\nlist_resource_keys_for_instance() result:')
            # begin-list_resource_keys_for_instance

            all_results = []
            pager = ResourceKeysForInstancePager(
                client=resource_controller_service,
                id=instance_guid,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_resource_keys_for_instance
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_binding_example(self):
        """
        delete_resource_binding request example
        """
        try:
            global binding_guid
            # begin-delete_resource_binding

            response = resource_controller_service.delete_resource_binding(id=binding_guid)

            # end-delete_resource_binding
            print('\ndelete_resource_binding() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_key_example(self):
        """
        delete_resource_key request example
        """
        try:
            global instance_key_guid
            # begin-delete_resource_key

            response = resource_controller_service.delete_resource_key(id=instance_key_guid)

            # end-delete_resource_key
            print('\ndelete_resource_key() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_alias_example(self):
        """
        delete_resource_alias request example
        """
        try:
            global alias_guid
            # begin-delete_resource_alias

            response = resource_controller_service.delete_resource_alias(id=alias_guid)

            # end-delete_resource_alias
            print('\ndelete_resource_alias() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_resource_instance_example(self):
        """
        lock_resource_instance request example
        """
        try:
            global instance_guid
            print('\nlock_resource_instance() result:')
            # begin-lock_resource_instance

            resource_instance = resource_controller_service.lock_resource_instance(id=instance_guid).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-lock_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_resource_instance_example(self):
        """
        unlock_resource_instance request example
        """
        try:
            global instance_guid
            print('\nunlock_resource_instance() result:')
            # begin-unlock_resource_instance

            resource_instance = resource_controller_service.unlock_resource_instance(id=instance_guid).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-unlock_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_instance_example(self):
        """
        delete_resource_instance request example
        """
        try:
            global instance_guid
            # begin-delete_resource_instance

            response = resource_controller_service.delete_resource_instance(id=instance_guid, recursive=False)

            # end-delete_resource_instance
            print('\ndelete_resource_instance() response status code: ', response.get_status_code())

            # wait for reclamation object to be created
            time.sleep(20)

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_reclamations_example(self):
        """
        list_reclamations request example
        """
        try:
            global instance_guid, reclamation_id, account_id
            print('\nlist_reclamations() result:')
            # begin-list_reclamations

            reclamations_list = resource_controller_service.list_reclamations(account_id=account_id).get_result()

            print(json.dumps(reclamations_list, indent=2))

            # end-list_reclamations

            for res in reclamations_list.get('resources'):
                if res.get('resource_instance_id') == instance_guid:
                    reclamation_id = res.get('id')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_run_reclamation_action_example(self):
        """
        run_reclamation_action request example
        """
        try:
            global reclamation_id
            assert reclamation_id is not None
            print('\nrun_reclamation_action() result:')
            # begin-run_reclamation_action

            reclamation = resource_controller_service.run_reclamation_action(
                id=reclamation_id, action_name='reclaim'
            ).get_result()

            print(json.dumps(reclamation, indent=2))

            # end-run_reclamation_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_cancel_lastop_resource_instance_example(self):
        """
        cancel_lastop_resource_instance request example
        """
        try:
            print('\ncancel_lastop_resource_instance() result:')
            # begin-cancel_lastop_resource_instance

            resource_instance = resource_controller_service.cancel_lastop_resource_instance(
                id=instance_guid
            ).get_result()
            print(json.dumps(resource_instance, indent=2))

            # end-cancel_lastop_resource_instance

        except ApiException as e:
            if e.message == "The instance is not cancelable.":
                print("The instance is not cancelable")
            else:
                pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: ResourceControllerV2
##############################################################################
