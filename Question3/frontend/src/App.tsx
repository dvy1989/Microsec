import * as React from 'react';
import './App.css';
import { Navbar, NavbarBrand, Alert } from 'reactstrap';
import { LoginForm } from './components/LginForm';
import { SensorList } from './components/SensorList';

interface IAppState {
  authentificated: boolean;
  errorStatus: number;
  token: string;
}

class App extends React.Component<{}, IAppState> {
  constructor(props: Readonly<{}>) {
    super(props);
    this.state = {
      authentificated: false,
      errorStatus: 0,
      token: ""
    };
  }

  public render() {
    return (
      <div>
        <Navbar color="primary">
          <NavbarBrand>Django Websocket application</NavbarBrand>
        </Navbar>
        <div className="p-5">
          {this.renderContent()}
        </div>
      </div>
    );
  }

  private renderContent(): React.ReactNode {
    if (!this.state.token) {
      return this.renderLoginForm();
    }
    switch (this.state.errorStatus) {
      case 500:
        return <Alert color="danger">Service unavailable</Alert>
      case 404:
        return <Alert color="danger">Service does not provide requested functionality</Alert>;
      case -100:
        return <Alert color="danger">Error in handling a response from the service</Alert>;
      case 401:
        return this.renderLoginForm();
      case 0:
        return <SensorList token={this.state.token} onLoadFailed={this.onLoadFailed} />
    }
    return <Alert color="warning">Some unexpected failure</Alert>
  }

  private renderLoginForm(): React.ReactNode {
    return <LoginForm onTokenObtained={this.setToken} />
  }

  private setToken = (obtainedToken: string) => this.setState({ token: obtainedToken });

  private onLoadFailed = () => this.setState({ errorStatus: 401 });
}

export default App;
