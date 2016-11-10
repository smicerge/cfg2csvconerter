# nagios defintions
# author : smicerge

# definitions =
# host.cfg


def conv_nag_hostdef(name):

    switcher = {
        'host_name': 0,
        'alias': 1,
        'display_name': 2,
        'address': 3,
        'parents': 4,
        'hostgroups': 5,
        'check_command': 6,
        'initial_state': 7,
        'max_check_attempts': 8,
        'check_interval': 9,
        'retry_interval': 10,
        'active_checks_enabled': 11,
        'passive_checks_enabled': 12,
        'check_period': 13,
        'obsess_over_host': 14,
        'check_freshness': 15,
        'freshness_threshold': 16,
        'event_handler': 17,
        'event_handler_enabled': 18,
        'low_flap_threshold': 19,
        'high_flap_threshold': 20,
        'flap_detection_enabled': 21,
        'flap_detection_options': 22,
        'process_perf_data': 23,
        'retain_status_information': 24,
        'retain_nonstatus_information': 25,
        'contacts': 26,
        'contact_groups': 27,
        'notification_interval': 28,
        'first_notification_delay': 29,
        'notification_period': 30,
        'notification_options': 31,
        'notifications_enabled': 32,
        'stalking_options': 33,
        'notes': 34,
        'notes_url': 35,
        'action_url': 36,
        'icon_image': 37,
        'icon_image_alt': 38,
        'vrml_image': 39,
        'statusmap_image': 40,
        '2d_coords': 41,
        '3d_coords': 42,
    }
    return int(switcher.get(name, 43))


def validatevalue(actlin):

    if actlin == '':
        return 'EMPTY'

    notok = ['{', '}']

    for actline in notok:
        if actline in actlin:
            return 'BAD'

    return 'OK'
