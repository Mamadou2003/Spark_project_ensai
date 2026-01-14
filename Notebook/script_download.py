import os
import requests
import yaml
from pathlib import Path
from typing import Dict, List

def load_config(yaml_path: str) -> Dict:

    with open(yaml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def download_file(url: str, output_path: str, timeout: int = 30) -> bool:
    """
    download a file from url
    
    Args:
        url: L'URL
        output_path: path to file
        timeout: sec
    
    Returns:
        bool
    """
    try:
        print(f"Downloading: {os.path.basename(output_path)}...", end=" ")
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        percent = (downloaded / total_size) * 100
                        print(f"\r{percent:.1f}%", end="")
        
        print(";)")
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def download_gas_prices(config: Dict) -> None:
    """
    download every gas prices
    
    Args:
        config: Dictionary containig:
            - data_directory: path to save the files
            - start_year: first year
            - end_year: last year
            - github_repo: 
    """
    base_url = config.get('github_repo', 'https://raw.githubusercontent.com/rvm-courses/GasPrices/main')
    output_dir = config.get('data_directory', '../Data/1-raw')
    start_year = config.get('start_year', 2022)
    end_year = config.get('end_year', 2024)
    
    print(f"\n Downloading from {start_year} to {end_year}")
    print(f" Destination: {output_dir}\n")
    
    files_to_download = []
    
    # Ajouter les fichiers de prix par année
    for year in range(start_year, end_year + 1):
        if year == 2022:
            # 2022 en deux parties
            files_to_download.append({
                'name': f'Prix{year}S1.csv.gz',
                'url': f'{base_url}/Prix{year}S1.csv.gz'
            })
            files_to_download.append({
                'name': f'Prix{year}S2.csv.gz',
                'url': f'{base_url}/Prix{year}S2.csv.gz'
            })
        else:
            files_to_download.append({
                'name': f'Prix{year}.csv.gz',
                'url': f'{base_url}/Prix{year}.csv.gz'
            })
    
    # Télécharger tous les fichiers
    success_count = 0
    for file_info in files_to_download:
        output_path = os.path.join(output_dir, file_info['name'])
        if download_file(file_info['url'], output_path):
            success_count += 1
    
    print(f"\nFINISHED: {success_count}/{len(files_to_download)} fichiers")

def main():
    """Load the config file"""
    # Charger la configuration
    config_path = 'config.yaml'
    
    if not os.path.exists(config_path):
        print(f"Fichier {config_path} not found!")
        print("We create the config file if not created by user default settings 2022 to 2024\n")
        
        default_config = {
            'data_directory': '../Data/1-raw',
            'start_year': 2022,
            'end_year': 2024,
            'github_repo': 'https://raw.githubusercontent.com/rvm-courses/GasPrices/main'
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(default_config, f, default_flow_style=False, allow_unicode=True)
        
        print(f" file {config_path} created\n")
        config = default_config
    else:
        config = load_config(config_path)
    
    download_gas_prices(config)

if __name__ == "__main__":
    main()