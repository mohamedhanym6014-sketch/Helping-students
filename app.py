# Dental-AI-Companion: Initial Prototype
# This is a simple CLI tool demonstrating the concept of the AI assistant for dental students.

def get_tooth_reduction_guide(tooth_type):
    """Provides a step-by-step guide for preclinical fixed prosthodontics tooth reduction."""
    guides = {
        "anterior": "1. Depth grooves (incisal 2mm, facial 1.5mm)\n2. Incisal reduction\n3. Facial reduction (two planes)\n4. Lingual clearance\n5. Proximal slices\n6. Finishing margins (Chamfer/Shoulder).",
        "posterior": "1. Occlusal depth grooves (1.5-2mm)\n2. Occlusal reduction following anatomy\n3. Functional cusp bevel\n4. Axial reduction\n5. Finishing margins."
    }
    return guides.get(tooth_type.lower(), "Guide not found. Please specify 'anterior' or 'posterior'.")

def analyze_simple_case(symptoms):
    """Simulates a basic clinical case analysis."""
    print(f"Analyzing symptoms: {symptoms}...")
    # Placeholder for future OpenAI API integration
    return "Suggestion: Proceed with vitality testing and periapical radiograph. (AI API integration pending)"

if __name__ == "__main__":
    print("🦷 Welcome to the Dental-AI-Companion Prototype!")
    print("-------------------------------------------------")
    print("Study Aid: Posterior Tooth Reduction Steps:")
    print(get_tooth_reduction_guide("posterior"))
    print("-------------------------------------------------")
    print("Clinical Simulation:")
    print(analyze_simple_case("Spontaneous lingering pain in lower right molar, sensitive to hot."))
