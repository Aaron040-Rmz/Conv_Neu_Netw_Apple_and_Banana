import argparse
import src.Capture_Manzana as manzana
import src.Capture_Platano as platano
import src.Trained_model as trainer
import src.Fruit_classifier as classifier

def main():
    parser = argparse.ArgumentParser(description="Herramienta para capturar, entrenar y clasificar frutas con red neuronal")
    parser.add_argument('--step', type=str, required=True, choices=[
        'capture_manzana', 'capture_platano', 'train', 'run'
    ], help="Selecciona el proceso que deseas ejecutar")

    args = parser.parse_args()

    # Mapeo de comandos
    if args.step == 'capture_manzana':
        print("[Proceso] Iniciando captura de imágenes: Manzana")
        manzana.capture_images()

    elif args.step == 'capture_platano':
        print("[Proceso] Iniciando captura de imágenes: Plátano")
        platano.capture_images()

    elif args.step == 'train':
        print("[Proceso] Entrenamiento del modelo en curso...")
        trainer.train_model()

    elif args.step == 'run':
        print("[Proceso] Ejecutando clasificador de frutas en vivo...")
        classifier.classify_image()

if __name__ == "__main__":
    # Punto de entrada principal
    main()
