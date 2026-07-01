"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
def test_constants():
    from ai_simple_engine_common.models.family_names import VAE_MODEL_FAMILY_NAME
    from ai_simple_engine_common.models.names import FACEBOOK_MUSICGEN_LARGE
    from ai_simple_engine_common.models.backends.provider_names import HUGGINGFACE_BACKEND_PROVIDER_NAME

    assert VAE_MODEL_FAMILY_NAME == 'vae'
    assert FACEBOOK_MUSICGEN_LARGE == 'facebook/musicgen-large'
    assert HUGGINGFACE_BACKEND_PROVIDER_NAME == 'huggingface'