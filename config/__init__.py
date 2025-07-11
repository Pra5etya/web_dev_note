import os

def register_config():
    env = os.getenv("FLASK_ENV").lower()

    if env == "production":
        from config.production import ProductionConfig

        print(f'\nUse production configuration')
        print('=' * 30)

        return ProductionConfig
    
    elif env == "staging":
        from config.staging import StagingConfig

        print(f'\nuse staging configuration')
        print('=' * 30)

        return StagingConfig
    
    else:
        from config.development import DevelopmentConfig

        print(f'\nUse development configuration')
        print('=' * 30)

        return DevelopmentConfig
