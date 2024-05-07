from app import dash_app, region_options


def test_app_initialization(dash_duo):
    dash_duo.start_server(dash_app)

    # Check if the header exists
    dash_duo.wait_for_element("#header", timeout=10)

    # Check if the radio button for region filtering exists
    dash_duo.wait_for_element("#region-filter", timeout=10)

    # Check if the visualization graph exists
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_radio_button_options(dash_duo):
    dash_duo.start_server(dash_app)

    # Check the options in the radio button
    options = dash_duo.find_element(
        "#region-filter").find_elements_by_tag_name("label")
    assert len(options) == len(region_options)
    for option, expected_option in zip(options, region_options):
        assert option.text == expected_option["label"]
