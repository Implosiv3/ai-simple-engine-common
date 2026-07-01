"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
def test_constants():
    from ai_simple_engine_common.consts.model_spec.families import VAE_MODEL_FAMILY
    from ai_simple_engine_common.consts.model_spec.identifiers import FACEBOOK_MUSICGEN_LARGE_MODEL_IDENTIFIER
    from ai_simple_engine_common.consts.model_spec.providers import HUGGINGFACE_MODEL_BACKEND_PROVIDER

    assert VAE_MODEL_FAMILY == 'vae'
    assert FACEBOOK_MUSICGEN_LARGE_MODEL_IDENTIFIER == 'facebook/musicgen-large'
    assert HUGGINGFACE_MODEL_BACKEND_PROVIDER == 'huggingface'