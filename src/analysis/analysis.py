import pandas as pd  # Importar Pandas para el manejo de datos
import os  # Importar os para operaciones del sistema operativo

# Constantes para rutas de archivos
DATA_PATH = "data/raw/products.csv"
OUTPUT_PATH = "data/processed/cleaned_products.csv"

def load_data(data_path):
    """Cargar datos desde CSV"""
    try:
        if data_path.endswith(".csv"):
            df = pd.read_csv(data_path)  # Cargar archivo CSV en DataFrame
        elif data_path.endswith(".xlsx"):
            df = pd.read_excel(data_path)  # Cargar archivo Excel en DataFrame
        else:
            raise ValueError("Unsupported file format")  # Levantar error si el formato de archivo no es compatible
        print("Data loaded successfully")  # Mostrar mensaje de éxito
        return df  # devolvemos el DataFrame con los datos
    except Exception as e:
        print(f"Error loading data: {str(e)}")  # Mostrar mensaje de error si falla la carga de datos

def clean_data(df):
    """Limpiamos los datos"""
    try:
        df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)  # Limpiar columna de precios
        print("Data cleaned successfully")  # Mostrar mensaje de éxito
        return df  # Retornar DataFrame limpio
    except Exception as e:
        print(f"Error cleaning data: {str(e)}")  # Mostrar mensaje de error si falla la limpieza de datos

def analyze_data(df):
    """Realizamos análisis básico de datos"""
    print("Basic data analysis:")
    print(df.describe())  # Mostrar las estadísticas básicas
    print("\nProducts with highest price:") # imprimimos los 5 productos más caros
    highestPrices = df.nlargest(5, "price")
    print(highestPrices)  # imprimimos los 5 productos más caros
        
def save_clean_data(df, output_path):
    """Guarda los datos limpios"""
    try:
        if output_path.endswith(".csv"):
            df.to_csv(output_path, index=False)  # Guardar DataFrame como archivo CSV
        elif output_path.endswith(".xlsx"):
            df.to_excel(output_path, index=False)  # Guardar DataFrame como archivo Excel
        else:
            raise ValueError("Unsupported file format")  # Levantar error si el formato de archivo no es compatible
        print(f"Clean data saved to {output_path}")  # Mostrar mensaje de éxito
    except Exception as e:
       print(f"Error saving data: {str(e)}")  # Mostrar mensaje de error si falla el guardado de datos


if __name__=="__main__":
    
    os.makedirs("data/processed", exist_ok=True)  # Crear directorio para datos procesados
    df = load_data(DATA_PATH)  # Cargar datos desde archivo al inicio
    df = clean_data(df)  # Limpiar datos al inicio
    df = analyze_data(df)  # Analizar datos al inicio
    save_clean_data(df, OUTPUT_PATH)  # Guardar datos limpios al inicio