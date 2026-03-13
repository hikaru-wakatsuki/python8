import sys
import importlib
from types import ModuleType


def check_package(name: str, message: str) -> ModuleType:
    try:
        module: ModuleType = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {message} ready")
        return module
    except ImportError:
        print(f"[MISSING] {name}")
        print("Install dependencies using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)


def main() -> None:
    try:
        print()
        print("LOADING STATUS: Loading programs...")
        print()
        print("Checking dependencies:")
        pandas: ModuleType = check_package("pandas", "Data manipulation")
        numpy: ModuleType = check_package("numpy", "Numerical computation")
        matplotlib: ModuleType = check_package("matplotlib", "Visualization")
        print()
        print("Analyzing Matrix data...")
        dice_min: int = 1
        dice_max: int = 6
        dice_data = numpy.random.randint(dice_min, dice_max + 1, 1000)
        print("Processing 1000 data points...")
        df = pandas.DataFrame({"dice_data": dice_data})
        print("Generating visualization...")
        import matplotlib.pyplot
        matplotlib.pyplot.figure()
        matplotlib.pyplot.hist(
            df["dice_data"], bins=numpy.arange(0.5, 7.5, 1), edgecolor="black")
        matplotlib.pyplot.title("Dice Roll Distribution")
        matplotlib.pyplot.xlabel("Dice Value")
        matplotlib.pyplot.ylabel("Frequency")
        output_file = "matrix_analysis.png"
        matplotlib.pyplot.savefig(output_file)
        print()
        print("Analysis complete!")
        print(f"Results saved to: {output_file}")
    except (PermissionError, TypeError, ValueError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
