from split_settings.tools import optional,include
base_settings = [
    'components/*.py',
    # 'development/*.py',
    'production/*.py'
]
include(*base_settings)