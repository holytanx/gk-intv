# React hook
## What is react hook?
= The function that can access react features: state management, side effect management, other..

## When to use react hook?
= When dev migrates class-based components (stateful) to functional-based components (stateless) and need react hook for making stateless to stateful for functional requirement.

## Basic react hooks:

- useState = use for state management such as when we change something on UI component: Add new item action => we wanna add new item into list, so useState can help you with that.

- useEffect = use for side-effect management such as when we want to change theme color when user click switch button turn off, the "useEffect" can detect and change something following the variable (in this case it's switch button turn off).

- useContext = use for sharing the global variables in entire app or nested components such as "user login status". In traditional way, we can pass down to every components (top to bottom) but maybe some component don't want it. So this is why we useContext, we don't need to pass down the props(variable). Just import function useContext and choose the context provider

## Other/additional hooks: 
https://reactjs.org/docs/hooks-reference.html