import * as React from 'react';
import { Form, FormGroup, Input, Label, Button } from 'reactstrap';
import axios, { AxiosResponse } from "axios";

interface ILoginFormState {
  password: string,
  username: string
}

interface ILoginFormProps {
  onTokenObtained: (token: string) => void;
}

export class LoginForm extends React.Component<ILoginFormProps, ILoginFormState> {
  private onTokenObtained: (token: string) => void;

  constructor(props: Readonly<ILoginFormProps>) {
    super(props);
    this.onTokenObtained = props.onTokenObtained;
    this.state = {
      password: "",
      username: ""
    };
  }

  public render(): React.ReactNode {
    return (
      <div className="container border rounded p-5 w-50">
        <Form>
          <h2 className="mb-3">Sign in</h2>
          <FormGroup>
            <Label for="username">Username</Label>
            <Input type="text" name="username" id="username" placeholder="Your user name" onChange={this.onLoginInputValueChanged} />
          </FormGroup>
          <FormGroup>
            <Label for="password">Password</Label>
            <Input type="password" name="password" id="password" onChange={this.onPasswordInputValueChanged} />
          </FormGroup>
          <Button color="primary" disabled={!this.state.username || !this.state.password} onClick={this.doLogin}>Sign in</Button>
        </Form>
      </div>);
  }

  private onLoginInputValueChanged = (e: React.FormEvent<HTMLInputElement>) => {
    this.setState({ username: e.currentTarget.value });
  }

  private onPasswordInputValueChanged = (e: React.FormEvent<HTMLInputElement>) => {
    this.setState({ password: e.currentTarget.value });
  }

  private doLogin = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    axios.post("http://localhost:8000/login", this.state).then(this.handleResponse);
  }

  private handleResponse = (response: AxiosResponse): void => {
    if (response.status === 200) {
      this.onTokenObtained(response.data.token);
    }
  }
}
