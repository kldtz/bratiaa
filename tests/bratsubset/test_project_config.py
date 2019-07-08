from bratsubset.projectconfig import ProjectConfiguration


def test_reading_entity_types():
    project_root = 'data/agreement/agree-2'
    config = ProjectConfiguration(project_root)
    assert config.get_entity_types() == ['ORG', 'PER', 'LOC', 'MISC']
