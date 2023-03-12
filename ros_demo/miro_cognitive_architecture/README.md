# Notes on MiRo Autonomous Mode
The miro demo controller has been developed on a brain based control architecture, where the focus is currently mainly based on the spinal cord and the brain-stem. The reference for this source code can be found in `~/mdk/share/python/miro2/core` and can be processed through `./client_demo.py`.

![MiRo Architecture](/miro_cognitive_architecture/miro_1.png)

In the client_demo, it can be noted that the most important bits of the control architecture would be based in `node_lower.py`, `node_affect.py`, `node_express.py`, `node_action.py`, and `node_loop.py`. These would be initialised where each `tick()` of these objects would allow the MiRo to process and produce behaviours based on sensory data and the current state of the MiRo. The `tick()` will be called as part of the callback function for the sensors package and the general flowchart can be described as follows.

![MiRo Architecture](/miro_cognitive_architecture/miro_1.png)

## Node Lower

The following node is set in the spinal cord where it will work through a freeze reflex. In this case, the MiRo would freeze when it determines that it is being petted on the head or the body itself. This would be determined based on how the interaction on the touch sensors could be determined as moving as a stroke onto it.

## Node Affect

In `node_affect.py`, it is mainly occupied with the computation and maintainence of the affective states of the MiRo which is part of the MiRo's brain-stem. This would be based on the emotion of the MiRo which is a two-dimensional state, i.e. the valence and arousal, and can be represented as follows:

![MiRo Architecture](/miro_cognitive_architecture/miro_affective.png)

This can be seen that the behaviours are dependent on the MiRo's emotion where various factors such as the exposure to light, time of the day, interaction such as touch or striking will update the affective states of the MiRo.

## Node Express

The following node describes the mood of the MiRo based on the LED based on its back and the movement of its cosmetic joints, i.e. movement of the eyes, ears and tail. This would change based on the valence and arousal of the MiRo itself.

## Node Action

The `node_action.py` consists of the basal-ganglia, which would act as the action-selector for the MiRo's set of action to produce behaviors, as well the freeze reflex and cliff reflex of the MiRo. In the case of the actions, this would be based on the child classes of `action/action_types.ActionTemplate` which would consist of methods that would allow the MiRo to re-arrange the priority of the actions,compute the action priortity and as such. This would be dependent on the different calculations fo the priority value in each of the actions, which are dependent on the nature of the behavior for the respective actions:
* action approach &rarr; based on locomotion componenets, valence, arousal
* action avert &rarr; set to turn away from stimulus
* action flee &rarr; based on locomotion componenets, valence, arousal
* action halt &rarr; debug filter/ check if stalling
* action mull &rarr; based on touch
* action orient &rarr; turn to visually foveate the stimulus
* action retreat &rarr; based on retreat distance
* action special &rarr; based on april tag

These would then be computed by the basal-ganglia where the behavior would be exhibited by a winner-takes-all action, thus stopping the previous action and starting a new one.

## Node Loop

The following node tries to express the MiRo based on features such as vocalization. This would mean that it would be dependent on the valence and arousal and this sample can be found on `client_voice_demo.py`