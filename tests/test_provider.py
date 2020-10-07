import pytest


def test_provider(fake_post_faker):
    fake_post_small = fake_post_faker.post()
    assert fake_post_small
    fake_post_medium = fake_post_faker.post(size='medium')
    assert fake_post_medium
    fake_post_large = fake_post_faker.post(size='large')
    assert fake_post_large


def test_provider_exception(fake_post_faker):
    with pytest.raises(ValueError):
        fake_post_faker.post(size='invalid_size')
