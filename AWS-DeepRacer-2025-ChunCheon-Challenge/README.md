# Technical Report: AWS DeepRacer 2025 ChunCheon Challenge

**Team Name:** 역시전략 (Yeoksi-Strategy)  
**Rank:** 3rd Place (Repechage Round)  
**Best Lap:** 00:17.225  
**Track:** A to Z Speedway (Clockwise, 2 Laps)  

---

## Abstract
This report documents the development and optimization of an autonomous racing agent for the 2025 ChunCheon AWS DeepRacer Championship. The primary objective was to navigate the 'A to Z Speedway' while autonomously avoiding static obstacles. We propose a **Zone-Based Reward Architecture** that dynamically adjusts hyperparameters based on track geometry (e.g., straightaways vs. hairpins). Furthermore, to address the **Sim2Real gap**, we implemented an active avoidance logic that incentivizes specific steering behaviors rather than merely penalizing collisions. This approach resulted in a stable lap time of 17.225 seconds and a 3rd place finish.

## 1. Introduction
Autonomous racing requires a delicate balance between speed maximization and stability control. In the context of AWS DeepRacer, Reinforcement Learning (RL) agents often suffer from overfitting to the simulation environment, leading to poor performance in physical tracks (Sim2Real gap). This project focuses on:
1.  **Geometric Decomposition:** Segmenting the track into functional zones to apply localized reward strategies.
2.  **Active Object Avoidance:** Transitioning from penalty-based avoidance to reward-based behavioral shaping.

## 2. Methodology: Reward Function Design

### 2.1 Geometric Track Segmentation (Zone-Based Approach)
We analyzed the curvature and optimal racing line of the 'A to Z Speedway' and classified the track into three distinct zones.

*   **Zone 1 (Equilibrium):** Moderate curvature. The reward function balances centerline adherence and velocity ($R \propto v \cdot (1 - d_{center})$).
*   **Zone 2 (Acceleration):** High-speed straight sections. The reward function applies a cubic weight to speed ($R \propto v^3$) to maximize throttle usage.
*   **Zone 3 (Control & Survival):** Acute hairpin turns. The priority shifts to steering precision. We introduced a logarithmic speed reward ($R \propto \log(v)$) to prevent reckless acceleration while maintaining momentum.

### 2.2 Active Obstacle Avoidance Logic
Early iterations relied on negative reinforcement (penalties) for collisions. However, this failed to teach the agent *how* to bypass obstacles, resulting in "freezing" behaviors in real-world tests.
To resolve this, we implemented an **Active Steering Incentive**:
*   **Condition:** When an obstacle is detected within a look-ahead distance of 1.0m.
*   **Action:** If the agent initiates a steering maneuver $> 20^\circ$ away from the obstacle, a positive reward (+2.0) is granted.
*   **Rationale:** This explicitly reinforces the *action* of evasion, rather than the *state* of safety.

## 3. Sim2Real Analysis and Optimization

### 3.1 The Reality Gap
During offline validation, the agent exhibited high variance in obstacle recognition. Simulation agents often learned to "teleport" past obstacles by exploiting physics engine quirks, which is impossible in reality.

### 3.2 Solution: Explicit Behavioral Guidance
Following expert consultation, we moved away from sparse rewards (pass/fail) to dense shaping rewards.
> *"Penalizing failure is insufficient; the agent must be rewarded for the correct corrective action."*

By rewarding the specific kinematic action of "steering away" when an object is detected, the agent learned a robust avoidance policy that generalized better to the physical robot's camera input delay and friction variances.

## 4. Conclusion
The proposed Zone-Based Reward Architecture successfully mitigated the trade-off between speed and stability. The inclusion of active steering incentives significantly reduced collision rates in the physical environment. Future work will focus on integrating proximal policy optimization (PPO) entropy tuning to further smooth the steering output.

---
*Repository Structure:*
*   `reward_functions/`: Iterative versions of the reward logic (Baseline to Final).
*   `assets/`: Visual data and performance graphs.
