import sys

hypothesis = {
    'h1': 0.1,
    'h2': 0.2,
    'h3': 0.4,
    'h4': 0.2,
    'h5': 0.1
}

candy_probabilities = {
    'h1': {'C': 1.0, 'L': 0.0},
    'h2': {'C': 0.75, 'L': 0.25},
    'h3': {'C': 0.50, 'L': 0.50},
    'h4': {'C': 0.25, 'L': 0.75},
    'h5': {'C': 0.0, 'L': 1.0}
}

observations = ""
updated_hypothesis = ""

def calculate_posterior(observations):
    observation_count = len(observations)
    posterior_probs = hypothesis.copy()
    global updated_hypothesis

    updated_hypothesis += f"Observation sequence Q: {observations}\n"
    updated_hypothesis += f"Length of Q: {observation_count}\n\n"

    for k in range(observation_count):
        updated_hypothesis += f"After Observation {k+1} = {observations[k]}:\n"
        for i in posterior_probs:
            if observations[k] == 'C':
                posterior_probs[i] *= candy_probabilities[i]['C']
            else:
                posterior_probs[i] *= candy_probabilities[i]['L']

        total_prob = sum(posterior_probs.values())
        for i in posterior_probs:
            posterior_probs[i] /= total_prob
            updated_hypothesis += f"P({i} | Q) = {posterior_probs[i]:.6f}\n"

        prob_c = sum(posterior_probs[h] * candy_probabilities[h]['C'] for h in posterior_probs)
        prob_l = sum(posterior_probs[h] * candy_probabilities[h]['L'] for h in posterior_probs)
        updated_hypothesis += f"\nProbability that the next candy we pick will be C, given Q: {prob_c:.6f}\n"
        updated_hypothesis += f"Probability that the next candy we pick will be L, given Q: {prob_l:.6f}\n\n"

    next_observation=updated_hypothesis
    write_to_file(next_observation)


def write_to_file(output_data):
    with open("result.txt", "w") as f:
        f.write(output_data)

def compute_a_posterior():
    global observations
    if len(sys.argv) > 1:
        observations = sys.argv[1]
    calculate_posterior(observations)


compute_a_posterior()
