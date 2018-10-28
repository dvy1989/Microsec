import * as React from 'react';
import './App.css';
import { Navbar, NavbarBrand, Alert } from 'reactstrap';

interface IAppState {
  authentificated: boolean;
  errorStatus: number;
}

class App extends React.Component<{}, IAppState> {
  constructor(props: Readonly<{}>) {
    super(props);
    this.state = {
      authentificated: false,
      errorStatus: 0
    };
  }

  public componentDidMount() {
    fetch("/api/sensors")
      .then(response => this.handleResponse(response))
      .catch((error) => this.setState({ errorStatus: -100 }));
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
    switch (this.state.errorStatus) {
      case 500:
        return <Alert color="danger">Service unavailable</Alert>
      case 404:
        return <Alert color="danger">Service does not provide requested functionality</Alert>;
      case -100:
          return <Alert color="danger">Error in handling a response from the service</Alert>;
      case 0:
        return <Alert color="dark">Sending a request...</Alert>
    }
    return <Alert color="warning">Some unexpected failure</Alert>
  }

  private handleResponse(response: Response): any {
    this.setState({ errorStatus: response.status, authentificated: response.status !== 200 });
  }
}

export default App;
