
from orchestrator import run_pipeline

query = input("Enter your research topic: ")
research, summary = run_pipeline(query)

print("\n--- Research Output ---\n", research)
print("\n--- Final Summary ---\n", summary)
